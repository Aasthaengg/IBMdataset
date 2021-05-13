x=int(input())
p=[100,101,102,103,104,105]
ans=[False]*2001
ans[0]=True
for i in range(2000):
    if ans[i]:
        for j in p:
            if i+j>2000:
                continue
            else:
                ans[i+j]=True
if x>2000:
    print(1)
elif ans[x]:
    print(1)
else:
    print(0)
