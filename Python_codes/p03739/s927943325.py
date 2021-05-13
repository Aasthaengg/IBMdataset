N = int(input())
A = list(map(int, input().split()))

def Cost(a, Sum):
    if Sum > 0:
        if Sum + a < 0:
            return 0
        else:
            return abs(Sum + a) + 1
    if Sum < 0:
        if Sum + a > 0:
            return 0
        else:
            return abs(Sum + a) + 1

Sum = lambda a, preSum:preSum + a if Cost(a, preSum) == 0 else (-1)**int(preSum > 0)

pCost, pSum = (lambda:(0, A[0]) if A[0] > 0 else (abs(A[0])+1, 1))()
nCost, nSum = (lambda:(0, A[0]) if A[0] < 0 else (abs(A[0])+1,-1))()
for a in A[1:]:
    pCost += Cost(a, pSum)
    pSum = Sum(a, pSum)
    nCost += Cost(a, nSum)
    nSum = Sum(a, nSum)
print(min(pCost, nCost))
