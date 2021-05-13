import re
s = input()
sub = re.sub('BC', 'X', s)

ans = 0
a = 0
for i in range(len(sub)):
    if sub[i] == 'A':
        a += 1
    elif sub[i] == 'X':
        ans += a
    else:
        a = 0

print(ans)