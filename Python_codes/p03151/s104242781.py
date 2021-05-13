from itertools import accumulate
n, *AB = map(int, open(0).read().split())
A, B = AB[:n], AB[n:]
P = []
N = []
for a, b in zip(A, B):
    if b-a > 0:
        P.append(b-a)
    elif b-a < 0:
        N.append(a-b)
N.sort(reverse=1)
s = sum(P)
if s == 0:
    print(0)
else:
    for i, x in enumerate(accumulate(N), 1):
        if x >= s:
            print(len(P) + i)
            break
    else:
        print(-1)