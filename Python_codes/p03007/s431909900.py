import sys
input = sys.stdin.readline

N = int(input())
As = list(map(int, input().split()))

history = []

positives = []
negatives = []
for A in As:
    if A >= 0:
        positives.append(A)
    else:
        negatives.append(A)

if not positives:
    n = max(negatives)
    negatives.remove(n)
    positives.append(n)

if not negatives:
    p = min(positives)
    positives.remove(p)
    negatives.append(p)

while len(negatives) > 1:
    p = positives.pop()
    n = negatives.pop()
    history.append((p, n))
    positives.append(p-n)

n = negatives[0]
while len(positives) > 1:
    p = positives.pop()
    history.append((n, p))
    n -= p

history.append((positives[0], n))
ans = positives[0] - n

print(ans)
for elem in history:
    print(*elem)