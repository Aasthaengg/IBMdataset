A,B,K=map(int,input().split())
count=0
while count!=K:
         if  A%2!=0:
                 A-=1
         A,B=A/2,A/2+B
         count+=1
         A,B=B,A
if count%2==0:
           print(int(A),int(B))
else:
            print(int(B),int(A))