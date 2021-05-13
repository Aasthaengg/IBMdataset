import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())
ans = 0
if (A + B) % 2 == 0:
    ans = (A + B)//2 - A
    print(ans)
else:
    ans = min(A, N-B+1)
    ans += (A + B)//2 - A
    print(ans)
