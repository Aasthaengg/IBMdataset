d=dict(zip([chr(i+97) for i in range(26)],[0]*26))
a=input()
n=len(a)
for i in a:
  d[i]+=1
ans=n*(n-1)//2+1
for i in d.values():
  ans-=i*(i-1)//2
print(ans)