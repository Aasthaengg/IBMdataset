N = int(input())
d = list(map(int,input().split()))
ans = 0
de = 0
for i in range(N):
    for j in range(N):
        ans +=  d[i]*d[j]
for k in range(N):
    de += d[k]**2
print(int((ans- de)/2))