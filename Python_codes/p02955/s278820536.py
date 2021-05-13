from itertools import accumulate

def getDivisor(x):
    ans = []
    for d in range(1, int(x**0.5)+1):
        if x%d == 0:
            ans.append(d)
            if x//d != d:
                ans.append(x//d)
    return sorted(ans)


N, K = map(int, input().split())
As = list(map(int, input().split()))

sumA = sum(As)
divisors = getDivisor(sumA)

def f(d):
    Bs = [A%d for A in As]
    Bs.sort()
    sumB = sum(Bs)
    accBs = list(accumulate(Bs))
    for i in range(1, N):
        numSub = accBs[i-1]
        numAdd = d*(N-i) - (sumB-accBs[i-1])
        if numSub <= K and numAdd <= K and (numSub-numAdd)%d == 0:
            return True
    return False


for d in reversed(divisors):
    ret = f(d)
    if ret:
        print(d)
        break
else:
    print(1)
