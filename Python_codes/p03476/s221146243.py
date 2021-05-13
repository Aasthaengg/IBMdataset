import math

def eratosthenes(n):
    prime_list = []
    num_list=[i for i in range(2, n+1)]
    limit = math.sqrt(n)
    while True:
        if limit <= num_list[0]:
            return prime_list + num_list
        prime_list.append(num_list[0])
        num_list = [e for e in num_list if e % num_list[0] != 0]

er_list = eratosthenes(100000)
count = [0]*100000
j = 0
for i in range(er_list[-1]):
    if i == er_list[j]:
        j += 1
        if (i+1)//2 in er_list:
            count[i] = 1 
            
for i in range(1,len(count)):
    count[i]  = count[i]+count[i-1]
    
Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    print(count[r]-count[l-1])