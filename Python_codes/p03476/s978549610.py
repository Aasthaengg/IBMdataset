import math
from itertools import accumulate

def eratosthenes(n):
    prime_list = []
    num_list=[i for i in range(2, n+1)]
    limit = math.sqrt(n)
    while True:
        if limit <= num_list[0]:
            return prime_list + num_list
        prime_list.append(num_list[0])
        num_list = [e for e in num_list if e % num_list[0] != 0]

        
Q = int(input())
l = [0]*Q
r = [0]*Q
for i in range(Q):
    l[i], r[i] = map(int, input().split())
    
max_r = max(r)+1
er_list = eratosthenes(max_r)
count = [0] * max_r


for i in range(len(er_list)):
    if (er_list[i]+1)//2 in er_list:
        count[er_list[i]] = 1
            
count = list(accumulate(count))
for i in range(Q):
    print(count[r[i]] - count[l[i]-1])
