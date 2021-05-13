# coding: utf-8
def Base_10_to_n(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    return out
    
N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
ans = float("inf")
for i in range(4**N):
    bits = Base_10_to_n(i, 4).zfill(N)
    a, b, c = 0, 0, 0
    cost = 0
    for j in range(len(bits)):
        if bits[j] == "0":
            pass
        elif bits[j] == "1":
            a += L[j]
            cost += 10
        elif bits[j] == "2":
            b += L[j]
            cost += 10
        else:
            c += L[j]
            cost += 10
    if min(a, b, c) > 0:
        ans = min(ans, cost + abs(a-A)+abs(b-B)+abs(c-C) - 10*3)
print(ans)