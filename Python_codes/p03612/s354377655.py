N = int(input())
p = list(map(int,input().split()))
cnt = 0
h = [p[i] == i + 1 for i in range(N)]
i = 1
while(i < N):
    if h[i] and h[i - 1]:
        cnt += 1
        i += 1
    i += 1
ans = sum(h) - cnt
print(ans)