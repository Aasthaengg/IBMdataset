from sys import stdin
N,Y=list(map(int,stdin.readline().strip().split()))
count=0
flag=False
if abs(N)-abs(Y)==0:
    print(1)
    exit()
if N>Y and abs(N)>abs(Y) or N>Y and N<0:
    count+=1
    N*=-1
    flag=True
YY=abs(Y)
NN=abs(N)
ans=0
if YY>NN:
    ans=YY-NN
else:
    ans=NN-YY
N+=ans
if Y==N:
    print(count+ans)
else:
    print(count+ans+1)