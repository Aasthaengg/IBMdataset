N, A, B = map(int, input().split())
 
s = A + B
ans = (N // s)*A
if (N % s) < A: print(ans + N % s)
else: print(ans + A)