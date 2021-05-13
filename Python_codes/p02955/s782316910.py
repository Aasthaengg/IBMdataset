import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,K = MI()
A = LI()

s = sum(A)

divisor = []  # s の約数

for i in range(1,int(s**.5)+1):
    if s % i == 0:
        divisor.append(i)
        if i != s//i:
            divisor.append((s//i))

divisor.sort(reverse=True)

from itertools import accumulate

for d in divisor:
    B = [a % d for a in A if a % d != 0]
    B.sort()
    C = [0] + list(accumulate(B))
    D = [0] + list(accumulate([d-b for b in B]))
    r = 10**10  # 操作の回数
    for i in range(len(C)):
        r = min(r,max(C[i],D[-1]-D[i]))
    if r <= K:
        print(d)
        break
