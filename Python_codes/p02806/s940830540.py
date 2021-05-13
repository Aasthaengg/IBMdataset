N = int(input())
st = [input().split() for i in range(N)]
X = input()
flg = 0
ans = 0
for s, t in st:
    if flg:
        ans += int(t)
    else:
        if s == X:
            flg = 1
print(ans)