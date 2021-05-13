N = int(input())
K = int(input())
X = int(input())
Y = int(input())

res = 0
for i in range(N):
    if i<= K-1:
        res += X
    else:
        res += Y
print(res)