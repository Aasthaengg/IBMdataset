N = int(input())
P = [int(input()) for i in range(N)]
ind = [0 for i in range(N)]
for i in range(N):
    ind[P[i]-1] = i
ans = 0
now = 1
for i in range(1,N):
    if ind[i] > ind[i-1]:
        now+=1
    else:
        ans = max(ans,now)
        now = 1
ans = max(ans,now)
print(N-ans)