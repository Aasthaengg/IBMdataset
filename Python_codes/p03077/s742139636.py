N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

div = min(A, B, C, D, E)
ans = (N-1)//div + 5
print(ans)