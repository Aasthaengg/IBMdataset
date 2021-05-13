N, D = map(int, input().split())
c = 0
for i in range(N):
    A, B = map(int, input().split())
    if A**2 + B**2 <= D**2:
        c += 1
print(c)