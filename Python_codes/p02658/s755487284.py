import sys
N = int(input())
A = list(map(int,input().split()))
product = 1
if 0 in A:
    print(0)
    sys.exit()
for i in range(N):
    product *= A[i]
    if product > 10 ** 18:
        product = -1
        break
print(product)