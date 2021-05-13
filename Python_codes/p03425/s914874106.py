from itertools import combinations


n = int(input())

s = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
for i in range(n):
    a = input()
    if a[0] in s.keys():
        s[a[0]] += 1

c = list(combinations(s.keys(), 3))
ans = 0
for i in c:
    ans += s[i[0]] * s[i[1]] * s[i[2]]

print(ans)
