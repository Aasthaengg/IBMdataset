from collections import Counter, deque

s = input()
n = len(s)
d = deque([{char} for char in s])
c = Counter(s)

if s[0] * n == s:
    print(0)
    exit()

for i in range(1, n):
    for j in range(n - i):
        char_j = s[j]
        char_right = s[j + i]
        set_j = d[j]
        if char_right not in set_j:
            set_j.add(char_right)
            c[char_right] += 1
    rightest = d.pop()
    for char in rightest:
        c[char] -= 1
    if max(c.values()) == n - i:
        print(i)
        exit()
print('oops, something wrong')
