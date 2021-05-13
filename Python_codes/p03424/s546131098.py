N=int(input())
S=list(map(str,input().split()))
flg=0
for i in range(N) :
  if S[i]=="Y" :
    flg=1
if flg==1 :
  print("Four")
else :
  print("Three")