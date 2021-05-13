n, k = map(int, input().split())
s = str(input())
h = 0
for i in range(1, n):
    if s[i] == 'L' and s[i-1] == 'L':
        h += 1
for i in range(n-1):
    if s[i] == 'R' and s[i+1] == 'R':
        h += 1
print(min(h + 2 * k, n - 1))