str = input()

n = len(str)
p = 0
ans = 0
for i in range(n):
    if str[i] == 'W':
        ans += i - p
        p += 1

print (ans)