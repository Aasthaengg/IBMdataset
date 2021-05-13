s = input()
k = int(input())
if len(s) == 1:
    print(k // 2)
    exit()

press = []
temp = s[0]
cnt = 0
for i in range(len(s)):
    if temp == s[i]:cnt += 1
    else:
        press.append((temp, cnt))
        cnt = 1
        temp = s[i]
press.append((temp, cnt))

if len(press) == 1:
    print(len(s) * k // 2)
    exit()

count = 0
for str, num in press:
    if num > 1:
        count += num // 2

count *= k
if s[0] == s[-1]:
    count -= (press[0][1] // 2 + press[-1][1] // 2 - (press[0][1] + press[-1][1]) // 2) * (k - 1)
print(count)