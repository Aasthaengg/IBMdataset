A,B,C,X = [int(input()) for _ in range(4)]
X = X//50

ans = 0

for i in range(min(A, X//10) + 1):
    Y = X - 10*i
    for j in range(min(B, Y//2) + 1):
        ans += Y - 2*j <= C

print(ans)