n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
over = []
short = 0
cnt = 0
for i in range(n):
    c = A[i] - B[i]
    if c > 0:
        over.append(c)
    elif c < 0:
        short -= c
        cnt += 1
if sum(over) < short:
    print(-1)
else:
    over.sort(reverse=True)
    s = 0
    i = 0
    while s < short:
        s += over[i]
        i += 1
    cnt += i
    print(cnt)
