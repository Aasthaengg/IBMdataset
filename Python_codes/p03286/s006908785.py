n = int(input())

ans = ""
cnt = 0

while n != 0:
    new = n - (-2) ** cnt
    if new % (2 ** (cnt + 1)) == 0:
        ans = "1" + ans
        n = n - (-2) ** cnt
    else:
        ans = "0" + ans
    cnt += 1

if not ans:
    print("0")
else:
    print(ans)
