N,K = map(int,input().split())
h = []
ans = 10**10
for i in range(N):
    tmp = int(input())
    h.append(tmp)
h = sorted(h)[::-1]
for i in range(N-K+1):
    ans = min(h[i]-h[i+K-1],ans)
print(str(ans))