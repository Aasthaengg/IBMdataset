N=int(input())
l=[input() for i in range(N)]
a_c=0
b_c=0
ab_c=0
ans=0
for i in l:
   ans+=i.count("AB")
   if i[0] == "B" and i[-1] == "A":
      ab_c+=1
      continue
   if i[-1] == "A":
      a_c+=1
   if i[0] == "B":
      b_c+=1
ans+=max(ab_c-1,0)
if a_c > 0 and ab_c>0:
   a_c-=1
   ans+=1
if b_c > 0 and ab_c>0:
   b_c-=1
   ans+=1
ans+=min(a_c,b_c)
print(ans)