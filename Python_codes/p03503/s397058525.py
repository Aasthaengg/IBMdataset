import itertools

n = int(input())
F_s = [list(map(int, input().split())) for _ in range(n)]
P_s = [list(map(int, input().split())) for _ in range(n)]

ans = -10 ** 10
flg = True
for lst in itertools.product(range(2), repeat = 10):
    if flg:
        flg = False
        continue
    ans_sub = 0
    for i in range(n):
        cnt = sum(j * k for j, k in zip(lst, F_s[i]))
        ans_sub += P_s[i][cnt]
    ans = max(ans, ans_sub)
print(ans)