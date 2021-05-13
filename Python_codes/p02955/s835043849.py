from itertools import accumulate

N, K = map(int, input().split())
As = list(map(int, input().split()))

def getDivisors(x):
    anss = set()
    for d in range(1, int(x**0.5)+1):
        if x%d == 0:
            anss.add(d)
            anss.add(x//d)
    return sorted(anss)

sumA = sum(As)
divs = getDivisors(sumA)

def check(x):
    Bs = [A%x for A in As if A%x]
    if not Bs:
        return True
    Bs.sort()
    accNums = list(accumulate(Bs))
    accNumRevs = list(accumulate([x-B for B in reversed(Bs)]))[::-1]
    for i in range(len(Bs)-1):
        if accNums[i] == accNumRevs[i+1] and accNums[i] <= K:
            return True
    return False

for div in reversed(divs):
    if check(div):
        print(div)
        break
