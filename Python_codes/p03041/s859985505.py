n,k = map(int,input().split())
S = list(input())
if(S[k-1]=="A"):
  S[k-1]="a"
elif(S[k-1]=="B"):
  S[k-1]="b"
else:
  S[k-1]="c"
for i in range(n):
  print(S[i],end='')