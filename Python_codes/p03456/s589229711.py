a,b=map(str,input().split())
x=int(a+b)
ans="No"
for i in range(100000):
    if x==i*i:
        ans="Yes"
print(ans)