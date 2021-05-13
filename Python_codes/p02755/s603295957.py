
A, B = map(int, input().split())


def floor_inv(x, f):
    res = int(x / f)
    if int(res * f) < x:
        res += 1
    return res


lb1 = floor_inv(A, 0.08)
ub1 = floor_inv(A + 1, 0.08)

lb2 = floor_inv(B, 0.10)
ub2 = floor_inv(B + 1, 0.10)

if ub1 <= lb2 or ub2 <= lb1:
    print(-1)
else:
    print(max(lb1, lb2))
