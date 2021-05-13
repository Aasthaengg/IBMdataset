from random import *
D=int(input())
C=list(map(int,input().split()))
S=[list(map(int,input().split())) for i in range(D)]
'''
ここはテスト用
D=365
C=[0]*26
S=[[0]*26 for i in range(D)]
for i in range(26):
  C[i]=randrange(0,101)
for i in range(D):
  for j in range(26):
    S[i][j]=randrange(0,20001)
'''
X=[0]*26
XX=X[:]
Y=X[:]
YY=X[:]
P=[]
SC=0
N,M,L,O,NN,MM=0,0,0,0,0,0
for i in range(D):
  for j in range(26):
    X[j]+=C[j]
    XX[j]+=X[j]
  N,M=-1,-10**20
  L,O=N,M
  NN,MM=N,M
  for j in range(26):
    if Y==-1:
      N,M=0,X[0]+S[i][0]
    if M<X[j]+S[i][j]:
      NN,MM=L,O
      L,O=N,M
      N,M=j,X[j]+S[i][j]
    elif O<X[j]+S[i][j]:
      NN,MM=L,O
      L,O=j,X[j]+S[i][j]
    elif MM<X[j]+S[i][j]:
      NN,MM=j,X[j]+S[i][j]
  XX[N]-=X[N]
  X[N]=0
  P.append([N,L,NN])
  SC+=X[N]
for i in range(D):
  SC2=SC
  d,q=i,P[i][1]
  SC2-=S[d][P[d][0]]
  SC2+=S[d][q]
  for j in range(26):
    Y[j]=0
  YY[P[d][0]],YY[q]=0,0
  for j in range(D):
    if j==d:
      Z=q
    else:
      Z=P[j][0]
    Y[P[d][0]]+=C[P[d][0]]
    Y[q]+=C[q]
    Y[Z]=0
    YY[P[d][0]]+=Y[P[d][0]]
    YY[q]+=Y[q]
  if SC2-sum(YY)>=SC-sum(XX):
    P[d]=[P[d][1],P[d][0],P[d][2]]
    XX=YY[:]
    SC=SC2
  SC2=SC
  d,q=i,P[i][2]
  SC2-=S[d][P[d][0]]
  SC2+=S[d][q]
  for j in range(26):
    Y[j]=0
  YY[P[d][0]],YY[q]=0,0
  for j in range(D):
    if j==d:
      Z=q
    else:
      Z=P[j][0]
    Y[P[d][0]]+=C[P[d][0]]
    Y[q]+=C[q]
    Y[Z]=0
    YY[P[d][0]]+=Y[P[d][0]]
    YY[q]+=Y[q]
  if SC2-sum(YY)>=SC-sum(XX):
    P[d]=[P[d][2],P[d][0],P[d][1]]
    XX=YY[:]
    SC=SC2
  SC2=SC
  d,q=i,P[i][1]
  SC2-=S[d][P[d][0]]
  SC2+=S[d][q]
  for j in range(26):
    Y[j]=0
  YY[P[d][0]],YY[q]=0,0
  for j in range(D):
    if j==d:
      Z=q
    else:
      Z=P[j][0]
    Y[P[d][0]]+=C[P[d][0]]
    Y[q]+=C[q]
    Y[Z]=0
    YY[P[d][0]]+=Y[P[d][0]]
    YY[q]+=Y[q]
  if SC2-sum(YY)>=SC-sum(XX):
    P[d]=[P[d][1],P[d][0],P[d][2]]
    XX=YY[:]
    SC=SC2
  SC2=SC
  d,q=i,P[i][2]
  SC2-=S[d][P[d][0]]
  SC2+=S[d][q]
  for j in range(26):
    Y[j]=0
  YY[P[d][0]],YY[q]=0,0
  for j in range(D):
    if j==d:
      Z=q
    else:
      Z=P[j][0]
    Y[P[d][0]]+=C[P[d][0]]
    Y[q]+=C[q]
    Y[Z]=0
    YY[P[d][0]]+=Y[P[d][0]]
    YY[q]+=Y[q]
  if SC2-sum(YY)>=SC-sum(XX):
    P[d]=[P[d][2],P[d][0],P[d][1]]
    XX=YY[:]
    SC=SC2
SC2=0
'''
ここちょっと消してみる
for i in range(10**5*3):
  d,q=randrange(0,D),randrange(0,26)
  SC2=SC
  SC2-=S[d][P[d][0]]
  SC2+=S[d][q]
  for j in range(26):
    Y[j]=0
  YY[P[d][0]],YY[q]=0,0
  for j in range(D):
    if j==d:
      Z=q
    else:
      Z=P[j][0]
    Y[P[d][0]]+=C[P[d][0]]
    Y[q]+=C[q]
    Y[Z]=0
    YY[P[d][0]]+=Y[P[d][0]]
    YY[q]+=Y[q]
  if SC2-sum(YY)>=SC-sum(XX):
    P[d][0]=q
    XX=YY[:]
    SC=SC2
'''
T=0
X=[0]*26
SC=0
for i in range(D):
  T=P[i][0]+1
  SC+=S[i][T-1]
  for j in range(26):
    X[j]+=C[j]
  X[T-1]=0
  SC-=sum(X)
  print(T)
#print(max(SC+10**6,0))