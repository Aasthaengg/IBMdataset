import sys
input = sys.stdin.readline

s = input()[:-1]
p, g = 0, 0
ans = 0

for si in s:
    if si=='g':
        if p<g:
            p += 1
            ans += 1
        else:
            g += 1
    else:
        if p<g:
            p += 1
        else:
            g += 1
            ans -= 1

print(ans)