N = int(input())
A = list(map(int,input().split()))
M = 1000005
l = [0 for i in range(M)]

for a in A:
    if l[a]!=0:
        l[a]+=1
        continue

    for i in range(a,M,a):
        l[i]+=1

ans = 0
for a in A:
    if l[a]==1:
        ans +=1

print(ans)