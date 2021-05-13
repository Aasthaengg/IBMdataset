import collections
N,M = map(int, input().split())
A = list(map(int,input().split()))
D = collections.Counter(A)

A.sort()
max = 0 

for i in range(M):
    B,C = map(int, input().split())
    D[C] += B  

D = sorted(D.items(), key=lambda x:x[0],reverse=True)

sum = 0 
count = 0 
for k,v in D:
    if N > v : 
        sum += k * v
        N -= v 
    else : 
        sum += k * N 
        break 
print(sum)