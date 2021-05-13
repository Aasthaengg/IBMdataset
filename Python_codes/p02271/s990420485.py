n1 = int(input())
A = list(map(int, input().split()))
n2 = int(input())
q = list(map(int, input().split()))

B = []
C = []
n = n1
ans = list("no" for i in range(n2))

for i in range(2 ** n):
    C0 = []
    B = list(map(int, format(i, "b").zfill(n)))[::-1]
    C0 = [ x*y for x, y in zip(A, B)]
    C.append(sum(C0))

for j, r in enumerate(q):    
    if  r in C:
        ans[j] = "yes"

print(*ans, sep="\n")