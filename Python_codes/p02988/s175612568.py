A=int(input())
l=list(map(int,input().split()))
ans=0
for i in range(A-2):
   tmp=l[i:i+3]
   tmp.sort()
   if tmp[1] == l[i+1]:
      ans+=1
print(ans)