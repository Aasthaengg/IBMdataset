n, k = [int(t) for t in input().split()]
w = [int(input()) for i in range(n)]

hi = sum(w)
lo = max(w)

def canMove(w, P, k):
    s = 0
    for i in range(len(w)):
        if s + w[i] > P:
            s = 0
            k -= 1
            if k <= 0: return False
        s += w[i]
    return True

P = hi
while lo < hi:
    m = (lo + hi) // 2
    if canMove(w, m, k):
        P = m
        hi = m
    else:
        lo = m + 1

print(P)

