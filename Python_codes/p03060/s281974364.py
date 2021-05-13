N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

B = 0
for i in range(N):
    b = V[i]-C[i]
    if b>=0:
        B = B + b
    else:
        pass

print(B)