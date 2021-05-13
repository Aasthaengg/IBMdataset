import sys
def I(): return int(sys.stdin.readline().rstrip())
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

s = LS2()
K = I()
n = len(s)

A = set()
for i in range(n):
    for j in range(i,min(n,i+5)):
        A.add(''.join(s[i:j+1]))

A = list(A)
A.sort()

print(A[K-1])
