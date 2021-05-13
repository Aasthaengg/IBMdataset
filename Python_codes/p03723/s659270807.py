import sys
A, B, C = map(int, input().split())

def isodd(x):
    if x % 2 == 1:
        return True
    else:
        return False

if isodd(A) or isodd(B) or isodd(C):
    print(0)
    sys.exit()
res = 0
while not isodd(A) and not isodd(B) and not isodd(C):
    if A == B == C:
        print(-1)
        sys.exit()
    tA, tB, tC = A, B, C
    A = tB//2 + tC//2
    B = tA//2 + tC//2
    C = tA//2 + tB//2
    res += 1
print(res)