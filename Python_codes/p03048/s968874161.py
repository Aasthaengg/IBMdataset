[A,B,C,N]=[int(i) for i in input().split()]
X=[A,B,C]
X.sort()
[C,B,A]=X
cnt=0
for i in range(N//A+1):
  k=N-(i*A)
  for j in range(k//B+1):
    if (k-(B*j))%C==0:
    	cnt+=1
print(cnt)