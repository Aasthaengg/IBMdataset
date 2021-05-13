n = int(input())

ans = 0
A = 0
B = 0
BA = 0
for _ in range(n):
    s = input()
    ans += s.count('AB')
    if (s[0], s[-1]) == ('B', 'A'):
        BA += 1
        continue
    if s[-1] == 'A':
        A += 1
    if s[0] == 'B':
        B += 1
else:
    if BA:
        ans += BA-1
        if A:
            A -= 1
            ans += 1
        if B:
            B -= 1
            ans += 1
    ans += min(A, B)
print(ans)
