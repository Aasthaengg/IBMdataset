s=input()
n=len(s)
b_cnt=s.count("B")
ans=0
for i in range(n):
  if s[i]=="B":
    ans+=n-b_cnt-i
    b_cnt-=1
print(ans)
