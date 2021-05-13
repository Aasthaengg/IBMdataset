N,M,X,Y = map(int,input().split())
XList = list(map(int,input().split()))
YList = list(map(int,input().split()))
if max(XList) >= max(YList):
  print('War')
  exit()
elif X >=Y:
  print('War')
  exit()
for item in range(X+1,Y+1):
  if max(XList) < item <= min(YList):
    print('No War')
    exit()
print('War')