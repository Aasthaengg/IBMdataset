from collections import Counter
n = int(input())
s = input()
e = int(s.count('E'))
ans = e

a = 0
for i in range(n):
    if s[i] == 'W':
        a += 1
    b = e - ((i+1)-a)
    ans = min(ans, a+b)


print(ans)