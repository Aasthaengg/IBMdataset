n=int(input())
L=list(map(int,input().split()))
L.sort()
if sum(L)-L[n-1]>L[n-1]:
  print('Yes')
else:
  print("No")