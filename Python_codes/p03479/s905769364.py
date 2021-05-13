import math

X,Y = map(int, input().split())

ans = []
for i in range(0, int(math.log2(10**18))+1):
    Z = X*pow(2, i)
    if Z<=Y:
        ans.append(Z)

print(len(ans))
