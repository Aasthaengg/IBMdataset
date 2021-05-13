n, k = map(int, input().split())
s = input()

happy = 0
rl = 0
before = s[0]
if before == 'R' and s[1] == 'R':
    happy += 1
for i in range(1, n):
    if before == 'R' and s[i] == 'L':
        rl += 1
    if s[i] == 'L' and s[i-1] == 'L':
        happy += 1
    if i < n-1:
        if s[i] == 'R' and s[i+1] == 'R':
            happy += 1
    before = s[i]

if rl < k:
    print(n-1)
else:
    print(happy + k*2)