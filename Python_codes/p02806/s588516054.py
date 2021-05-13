n = int(input())
ST = [list(map(str, input().split())) for _ in range(n)]
X = input()

cnt = 0
flg = False
for s, t in ST:
    if flg:
        cnt += int(t)
    if s == X:
        flg = True

print(cnt)