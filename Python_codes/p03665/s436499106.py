N, P = map(int, input().split())
A = list(map(int, input().split()))
ev = 0
od = 0
for a in A:
    if a % 2 == 0:
        ev += 1
    else:
        od += 1
if P == 0 and od == 0:
    print(2**ev)
else:
    print(2**ev * (2**od//2))
