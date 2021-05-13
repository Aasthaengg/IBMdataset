N = int(input())
K = int(input())
X = [int(k) for k in input().split()]
X = [-1] + X
# print(X)
result = 0

for i in range(len(X)):
    if (i != 0):
        # print(
        #     "i = "+str(i)+", X[i] = "+str(X[i])
        # )
        A = X[i]
        B = abs(K - X[i])
        # print(
        #     "A = "+str(A)+", B = "+str(B)
        # )
        if (A > B):
            result += B*2
        else:
            result += A*2

print(result)
