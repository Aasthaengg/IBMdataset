N = int(input())
ba, bc, ca = 0, 0, 0
c = 0
for _ in range(N):
    ss = input()
    if ss[0] == 'B':
        if ss[-1] =='A':
            ba += 1
        else: bc += 1
    else:
        if ss[-1] == 'A':
            ca += 1
    c += ss.count('AB')

cnt = max(ba - 1, 0)
if ba >= 1:
    if ca >= 1:
        ca -= 1
        cnt += 1
    if bc >= 1:
        bc -= 1
        cnt += 1
cnt += min(ca, bc)

print(cnt + c)