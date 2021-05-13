s = input().rstrip()
n = len(s)
ans = n * (n-1) // 2

from string import ascii_lowercase

for c in ascii_lowercase:
    m = s.count(c)
    ans -= m * (m-1) // 2

print(ans + 1)