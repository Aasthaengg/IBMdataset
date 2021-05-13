n = int(input())

cnt = 0
BA = 0
B_ = 0
_A = 0
for _ in range(n):
    s = input()
    cnt += s.count('AB')
    if s[0] == 'B' and s[-1] == 'A':
        BA += 1
    elif s[0] == 'B':
        B_ += 1
    elif s[-1] == 'A':
        _A += 1

if BA:
    cnt += BA - 1
    if B_:
        cnt += 1
        B_ -= 1
    if _A:
        cnt += 1
        _A -= 1
cnt += min(max(0, B_), max(0, _A))

print(cnt)
