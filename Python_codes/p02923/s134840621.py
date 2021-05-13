N=int(input())
*H,=map(int,input().split())


i=cnt=ans=0
while i<N-1:
 if 1<=H[i]/H[i+1]:
   cnt+=1
 else:
   ans=max(ans,cnt)
   cnt=0
 i+=1
print(max(ans,cnt))