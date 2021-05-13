n, k =map(int, input().split())
hitpoint=list(map(int,input().split()))
hitpoint.sort()
exe=[0]*k
if k!=0:
  hitpoint[-k:]=exe
  print(sum(hitpoint))
  exit(0)
else:
  print(sum(hitpoint))