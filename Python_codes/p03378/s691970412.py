N,M,X = map(int,input().split())
As=list(map(int,input().split()))

toN =0
to0 =0

for i in range(X+1,N):
  if i in As:
    toN +=1
for i in range(X-1,0,-1):
  if i in As:
    to0 +=1
print(min(toN,to0))