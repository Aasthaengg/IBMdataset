import sys
N, A, B = map(int, input().split())
if (B-A) % 2 == 0:
    ans = (B-A)//2
    print(ans)
    sys.exit()
if A-1 <= N-B:
    ans = A
    B -= A
    A = 1
else:
    ans = N-B+1
    A += ans
    B = N
if A != B:
    ans = ans+(B-A)//2
print(ans)
