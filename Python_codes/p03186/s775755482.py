A,B,C = map(int, input().split())

ans = 0
if C>=(B):
    ans = ans + 2*B
    C = C - (B)
    if C<0:
        C = 0
    ans = ans + min(A, C)
    C = C - min(A,C)
    ans = ans + min(C, 1)
    print(ans)
else:
    print(B+C)