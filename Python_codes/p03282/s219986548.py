S=list(input())
K=int(input())
#print(S)
i=0;p=0;q=0
while i!=len(S):
  if S[i]!="1":
    p=1
    q=i
    if K<i+1:
      print("1")
    else:
      print(S[i])
    break
  i=i+1
if p==0:
  print("1")