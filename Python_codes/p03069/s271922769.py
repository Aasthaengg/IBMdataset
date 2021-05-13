n = int(input())
s = input()
white, black = s.count('.'), 0
ans = white+black

for i in s:
    if i == '#':
        black += 1
    else:
        white -= 1
    ans = min(ans, white+black)
print(ans)
