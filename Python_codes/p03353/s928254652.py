import sys
# input処理を高速化する
input = lambda: sys.stdin.readline().rstrip()

s = input()
K = int(input())

N = len(s)
subst = set()
for i in range(N):
    for j in range(1,K+1):
        subst.add(s[i:min(i+j, N)])
print(sorted(subst)[K-1])