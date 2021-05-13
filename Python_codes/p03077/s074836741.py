N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())


mi = min(A, B, C, D, E)

s = 0 if N % mi == 0 else 1
ans = 5 if mi > N else 4+N//mi+s
print(ans)