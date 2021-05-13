N ,K = map(int,input().split())
li   =list(map(int,input().split()))
ans = 0
li.sort()
for l in li[N-K:N]:
    ans = ans + int(l)
print(str(ans))