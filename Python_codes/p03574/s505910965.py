H,W=map(int,input().split())
s=[['.']*(W+2) for i in range(H+2)]
for i in range(H):
  S=input()
  t='.'+S+'.'
  s[i+1]=t
for i in range(H):
  for j in range(W):
    b=0
    if s[i+1][j+1]!='#':
      for k in range(-1,2,1):
        for l in range(-1,2,1):
          if s[i+1+k][j+1+l]=='#':
            b+=1
    else:
      b='#'
    print(b,end='')
  print()