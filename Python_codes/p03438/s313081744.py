import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))

if A == B:
    print("Yes")
    exit()
diff = [a - b for a, b in zip(A, B)]
minus = []
plus = []
for d in diff:
    if d < 0:
        minus.append(-d)
    elif d > 0:
        plus.append(d)

total = 2 * sum(plus)
minus.sort()
while total:
    if not minus or sum(minus) < total:
        break
    if minus[-1] >= total:
        total = 0
    else:
        if minus[-1] % 2 == 1:
            total -= minus[-1] - 1
        else:
            total -= minus[-1]
        minus.pop()
else:
    print("Yes")
    exit()
print("No")