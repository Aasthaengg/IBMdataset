s = input()
k = int(input())


first = 0

for i in range(1, len(s)):
    if s[i] != s[0]:
        first = i
        break

if first == 0:
    if len(s) % 2 == 0:
        print((len(s) // 2) * k)
    else:
        print(len(s) * k // 2)
    exit()

ans = 0
cnt = 1
i = 0

while i < len(s) - 1:
    if s[i] == s[i+1]:
        cnt += 1
        if i == len(s) - 2:
            ans += cnt // 2
    else:
        ans += cnt // 2
        cnt = 1
    i += 1

ans *= k

if s[0] == s[-1] and first % 2 == 1 and cnt % 2 == 1:
    ans += k - 1

print(ans)
