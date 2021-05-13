n = int(input())
x,y,z = 0,0,0
ans = 0
for _ in range(n):
    s = input()
    for i in range(len(s)-1):
        if s[i] == 'A' and s[i+1] == 'B':
            ans += 1
    if s[0] == 'B' and s[-1] == 'A':
        x += 1
    elif s[0] == 'B':
        y += 1
    elif s[-1] == 'A':
        z += 1
    else:
        pass
if x == 0:
    print(ans+min(y,z))
else:
    if y + z > 0:
        print(ans + x + min(y,z))
    else:
        print(ans + x - 1)