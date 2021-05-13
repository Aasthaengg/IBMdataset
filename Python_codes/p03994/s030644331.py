t="abcdefghijklmnopqrstuvwxyz"
s=input()
k=int(input())
a=[t.index(i)for i in s]
ans=""
for i in a:
  j=i
  if i==0:
    ans+="a"
    continue
  if k>=26-i:
    k-=26-i
    j=0
  ans+=t[j]
j+=k
j%=26
ans=ans[:-1]+t[j]
print(ans)