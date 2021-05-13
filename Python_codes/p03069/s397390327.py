n = int(input())
S = input()

rw = S.count('.')
rb = S.count('#')
lw = 0
lb = 0

ans = min(rb, rw)
for s in S:
    if s == '.':
        lw += 1
        rw -= 1
    else:
        lb += 1
        rb -= 1
    ans = min(ans, lb+rw)
print(ans)
