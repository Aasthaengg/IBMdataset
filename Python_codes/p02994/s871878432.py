N, L = map(int, input().split())

ans = 0
flag = False
for i in range(N):
    if L + i == 0:
        flag = True
    ans += (L + i)
if not flag:
    if ans < 0:
        ans -= (L+N-1)
    else:
        ans -= L
print(ans)