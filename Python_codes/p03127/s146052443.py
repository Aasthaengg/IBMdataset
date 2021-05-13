N = int(input())
A = list(map(int, input().split()))

mn = min(A)
while True:
    ok = False
    for a in A:
        x = a % mn
        if x != 0 and x < mn:
            mn = x
            ok = True
    if not ok:
        break
print(mn)