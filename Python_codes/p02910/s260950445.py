s = input()
n = len(s)
ans = 0

for i in range(n):
    if i % 2 == 0:
        if s[i] != 'L':
            ans += 1
    else:
        if s[i] != 'R':
            ans += 1
            
if ans == n:
    print('Yes')
else:
    print('No')