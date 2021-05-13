N = int(input())
A = list(map(int,input().split(' ')))

ans=1
thresh=10**18
A.sort()
for i in range(N):
    ans = ans * A[i]
    if ans > thresh:
        ans=-1
        break

print(ans)