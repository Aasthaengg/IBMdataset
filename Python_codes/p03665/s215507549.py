import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
N,P = map(int,input().split())
A = list(map(int, input().split()))
oddC = 0
evenC = 0
for a in A:
    if a % 2 == 1:
        oddC += 1
    else:
        evenC += 1
c = 0
if P == 0:
    oddcombi = 0
    for i in range(oddC+1):
        if i % 2 == 1:
            continue
        oddcombi += combinations_count(oddC,i)
    evencombi = 0
    for i in range(evenC+1):
        evencombi += combinations_count(evenC,i)
    print(oddcombi*evencombi)
else:
    oddcombi = 0
    for i in range(oddC+1):
        if i % 2 == 0:
            continue
        oddcombi += combinations_count(oddC,i)
    evencombi = 0
    for i in range(evenC+1):
        evencombi += combinations_count(evenC,i)
    print(oddcombi*evencombi)
