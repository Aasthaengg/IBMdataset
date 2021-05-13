import sys

def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,M = LI()
A = LI()

B = [0]
for i in range(N):
    B.append((B[-1]+A[i]) % M)

from collections import Counter

count = Counter(B)

ans = 0
for i in count.keys():
    ans += count[i]*(count[i]-1)//2

print(ans)