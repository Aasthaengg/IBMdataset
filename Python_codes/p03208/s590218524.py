import sys
input = sys.stdin.readline
maxa=10**10
L=list()
N,K=map(int,input().split())
for i in range(N):
  S=int(input())
  L.append(S)
L=sorted(L)
for i in range(N-K+1):
  maxa=min(maxa,L[i+K-1]-L[i])
print(maxa)