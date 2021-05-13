# dekinakatta!!
import math
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    a = int(math.log2(max(A))) + 1
    l = [0] * a
    for i in A:
        t = 0
        while i > 0:
            if i % 2 == 1:
                l[t] += 1
            i >>= 1
            t += 1
    la = [0 if i >= (N-i) else 1 for i in l]
    lla = sum(v * pow(2,i) for i, v in enumerate(la))
    lk = []
    K2 = K
    while K2 > 0:
        if K2 % 2 == 1:
            lk.append(1)
        else:
            lk.append(0)
        K2 >>= 1
    if len(lk) > len(la):
        la.extend([0] * (len(lk)-len(la)))
        l.extend([0] * (len(lk)-len(l)))
    else:
        lk.extend([0] * (len(la)-len(lk)))
    r = sum(pow(2, i) * l[i] for i in range(len(l)))
    for i in range(len(lk)):
        if lk[i] == 1:
            r = max(r, calc(lk, la, N, l, i))
    t = 0
    for i in range(len(lk)):
        if lk[i] == 1:
            t += pow(2, i) * max(l[i], N - l[i])
        else:
            t += pow(2, i) * l[i]
    r = max(r, t)
    return r

def calc(lk, la, N, l, j):
    r = 0
    for i in range(j):
        r += pow(2, i) * max(l[i], N - l[i])
    r += pow(2, j) * l[j]
    for i in range(j+1, len(lk)):
        if lk[i] == 1:
            r += pow(2, i) * max(l[i], N - l[i])
        else:
            r += pow(2, i) * l[i]
    return r
print(main())
