t=input()
s=list(t)
k=int(input())

# 全部同じ文字の場合
if s==[s[0]]*len(s):
  print((len(s)*k)//2)
  exit()

b=[1]
for i in range(1,len(s)):
  if s[i-1]==s[i]:
      b[-1]+=1
  else:
      b.append(1)

ans=0
for i in b:
    ans+=i//2*k

if t[0]==t[-1] and (b[0]+b[-1])%2==0:
    ans+=k-1
print(ans)