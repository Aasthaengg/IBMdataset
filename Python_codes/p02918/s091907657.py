import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = input()

res = [0]
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        res[-1] += 1
    else:
        res.append(0)
print(min(sum(res) + 2 * m, n - 1))
