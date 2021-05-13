s = input()
from string import ascii_lowercase as abc
ans = 1000
for i in abc:
    ans = min(ans, max(list(map(len, s.split(i)))))
print(ans)
