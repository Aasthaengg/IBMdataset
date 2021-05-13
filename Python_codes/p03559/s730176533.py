N=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
answer=0

#それぞれのリストを小さい順に並べる
A.sort()
B.sort()
C.sort()

#ソートしたA[i]に対してそれより大きいBの要素数
Acount=[]
#同様にB[i]に対してC
Bcount=[]
#Bcountを後ろから取った累積和
Bsum=[]

count=0
for i in range(N):
  while(count!=N and A[i]>=B[count]): 
    count+=1
  Acount.append(N-count)

count=0
for i in range(N):
  while(count!=N and B[i]>=C[count]):
    count+=1
  Bcount.append(N-count) #いらんかった
  
Bsum.append(Bcount[N-1])



for i in range(1,N):
  Bsum.append(Bcount[N-i-1]+Bsum[i-1])

for i in range(N):
  if Acount[i]==0:
    print(answer)
    exit()
  answer+=Bsum[Acount[i]-1]
print(answer)