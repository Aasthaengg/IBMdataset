N = int(input())
lis = [0] * N
for i in range(N):
    P = int(input())
    P -= 1
    lis[P] = i
ans = 1
cnt = 1
for i in range(1,N):
    if lis[i] < lis[i-1]:
        cnt = 0
    cnt += 1
    ans = max(ans,cnt)
print(N-ans)
