n = int(input())

_a = 0
b_ = 0
b_a = 0

cnt = 0

for i in range(n):
    s = input()

    sa = False
    sb = False
    if s[0] == "B":
        sb = True
    if s[-1] == "A":
        sa = True

    if sa and sb:
        b_a += 1
    elif sa:
        _a += 1
    elif sb:
        b_ += 1

    for j in range(len(s)-1):
        if s[j:j+2] == "AB":
            cnt += 1

if b_a > 0:
    cnt += b_a - 1
    if _a >= 1:
        _a -= 1
        cnt += 1
    if b_ >= 1:
        b_ -= 1
        cnt += 1

cnt += min(_a, b_)
print(cnt)