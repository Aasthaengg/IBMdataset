N, D = map(int, input().split())
cnt = 0

for i in range(N):
    Z = input()
    Z = Z.split()
    X = int(Z[0])
    Y = int(Z[1])
    if X**2 + Y**2 <= D**2:
        cnt += 1
print(cnt)
