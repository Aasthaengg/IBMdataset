N,K=list(map(int,input().split()))
l=input()
n=l[0]
cnt=0
ans=[]
for i in l:
   if i != n:
      ans.append(cnt)
      cnt=1
      n=i
   else:
      cnt+=1
ans.append(cnt)
if l[0] == "0":
   sum_n=sum(ans[0:K*2])
   now=1
   end=K*2
   plus=0
else:
   sum_n=sum(ans[0:K*2+1])
   now=0
   end=K*2+1
   plus=1
max_n=sum_n
for i in range(len(ans)-end+plus):
   sum_n-=ans[i]
   if now==0:
      now=1
   else:
      try:
         sum_n=sum_n+ans[end]+ans[end+1]
         end+=2
      except IndexError:
         sum_n+=ans[end]
         max_n=max(sum_n,max_n)
         print(max_n)
         exit()
      now=0
   max_n=max(sum_n,max_n)
print(max_n)