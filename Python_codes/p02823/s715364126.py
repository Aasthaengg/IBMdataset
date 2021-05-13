N, A, B = map(int, input().split())

if (B-A) % 2 == 0:
    ans = (B-A+2)//2-1
else:
    if min(A-1, N-B) == A-1:
        ans = B-1
        plus=A
        B -= A
        A = 1
    else:
        ans = N-A
        plus=N-B+1
        A += N-B+1
        B = N
    if A != B:
        ans = (B-A+2)//2-1+plus

print(ans)
