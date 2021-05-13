N, K= map(int, input().split()) 
p = list(map(int, input().split()))
A=sorted(p)
s=0
for i in range(K):
    s=s+A[i]
print(s)
