li=list(map(int,input().split()))
ans=[]
a=li[0]*li[2]
b=li[0]*li[3]
c=li[1]*li[2]
d=li[1]*li[3]
ans.append(a)
ans.append(b)
ans.append(c)
ans.append(d)

print(max(ans))
