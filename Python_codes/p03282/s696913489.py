s = input()
k = int(input())
cnt = 0
for i in range(len(s)):
    if s[i] != "1":
        x = s[i]
        break
    else:
        cnt += 1
if cnt >= k:
    print(1)
else:
    print(x)