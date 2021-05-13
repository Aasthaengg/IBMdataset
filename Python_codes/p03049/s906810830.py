n = int(input())
AB = 0
A_B = 0
A = 0
B = 0
for _ in range(n):
    s = input()
    AB += s.count('AB')
    if s[0] == 'B' and s[-1] == 'A':
        A_B += 1
        continue
    if s[0] == 'B':
        B += 1
    if s[-1] == 'A':
        A += 1
ans = 0
if A_B == 0:
    ans = AB + min(B, A)
else:
    if A + B:
        ans = AB + A_B + min(B, A)
    else:
        ans = AB + A_B - 1
print(ans)
