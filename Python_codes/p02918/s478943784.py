n, k = map(int,input().split())
s = input()

press = []
temp = s[0]
cnt = 0
for string in s:
    if temp == string:
        cnt += 1
    else:
        press.append(cnt)
        temp = string
        cnt = 1
press.append(cnt)

if len(press) - 2 * k <= 0:
    print(n-1)
    exit()

ans = 2 * k
for i in press:
    ans += i - 1
print(ans)