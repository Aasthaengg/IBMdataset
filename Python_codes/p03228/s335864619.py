A,B,K=map(int,input().split())
while K>0:
 A,B=A//2,B+A//2;K-=1
 if K==0:break
 B,A=B//2,A+B//2;K-=1
print(A,B)