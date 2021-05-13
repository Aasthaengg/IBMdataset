import sys
N=int(input())
L=list(map(int,input().split()))
c=sum(L)
for i in range(N):
  if L[i]>=c-L[i]:
    print("No")
    sys.exit()
print("Yes")