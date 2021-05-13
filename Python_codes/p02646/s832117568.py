A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
Vf = V - W
D = abs(A - B)
Df = D - Vf * T
if Df <= 0:
    print("YES")
else:
    print("NO")