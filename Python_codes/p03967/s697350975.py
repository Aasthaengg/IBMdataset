s = input()
lis = []
for i in range(len(s)):
    if s[i] == 'g':
        lis.append(0)
    else:
        lis.append(1)
ans = 0
for i in range(len(s)):
    ans += i%2 - lis[i]
print(ans)
