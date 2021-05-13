n, k = map(int, input().split())
s = input()

ln, rn = 0, 0

i = 0
while i < n:
    if s[i] == 'R':
        while i < n and s[i] == 'R':
            i += 1
        rn += 1
    if i < n and s[i] == 'L':
        while i < n and s[i] == 'L':
            i += 1
        ln += 1
m = min(ln, rn)
if m > k:
    if ln == rn:
        print(n - 2 * (m - k))
    else:
        print(n - 2 * (m - k) - 1)
else:
    print(n - 1)