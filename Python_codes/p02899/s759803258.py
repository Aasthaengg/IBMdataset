import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
Ac = list(range(1,N+1))
Alis = [[i,j]  for i,j in zip(A,Ac)]
As = sorted(Alis)
for a in As:
    print(a[1],end = " ")