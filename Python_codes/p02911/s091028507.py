N,K,Q = map(int,input().split())
cnt = [0]*N

for i in range(Q):
    s = int(input())
    cnt[s-1] += 1

for j in range(N):
    ans = K - Q + cnt[j]
    if ans > 0:
        print("Yes")
    else:print("No")