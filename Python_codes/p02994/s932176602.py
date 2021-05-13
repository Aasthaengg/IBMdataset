n,l=map(int,input().split())

t=[] #各リンゴの味

for i in range(1,n+1):
  a=l+i-1
  t.append(a)

t_total=sum(t) #N個のリンゴの味の総和


t2=[] #全リンゴの味の総和から1個のリンゴを引いたもの味

for j in t:
  b=t_total-j
  t2.append(b)

ans=[]

for k in t2:
  c=t_total-k
  ans.append(abs(c))

ind=ans.index(min(ans))

print(t_total-t[ind])