import sys

s = input()
first = s.find('B')

if first == -1:
    print(0)
    sys.exit()

ans = 0
for i in range(first + 1, len(s)):
    if s[i] == 'W':
        ans += i - first
        first += 1

print(ans)