n=input().rstrip().split()
preans=(int(n[0])-1)/(int(n[1])-1)
 
ans=int(preans)
if (int(n[0])-1)%(int(n[1])-1)!=0:
  ans+=1
print(ans)