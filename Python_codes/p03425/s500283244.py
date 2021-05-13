from itertools import combinations
n = int(input())
march = [0 for _ in range(5)]
for i in range(n):
    s = input()

    if s[0] == 'M':
        march[0] += 1
    elif s[0] == 'A':
        march[1] += 1
    elif s[0] == 'R':
        march[2] += 1
    elif s[0] == 'C':
        march[3] += 1
    elif s[0] == 'H':
        march[4] += 1
ans = 0
for i in combinations(range(5), 3):
    ans += march[i[0]] * march[i[1]] * march[i[2]]
print(ans)
