a,b=[int(x) for x in input().split()]
ans=1
for i in range(1,30):
    c=a*1+(a-1)*(i-1)
    if c>=b:
        ans=i
        break
if b==1:
    print(0)
else:
    print(ans)