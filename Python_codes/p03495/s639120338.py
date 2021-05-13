from collections import Counter

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

cntA = Counter(A)
cntvalA = sorted(list(cntA.values()))
ans = sum(cntvalA[i] for i in range(len(cntvalA) - K))
print(ans)