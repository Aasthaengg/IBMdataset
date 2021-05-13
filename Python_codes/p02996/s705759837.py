N=int(input())
Z=[]
for i in range(N):
    Z.append(list(map(int,input().split())))
ct=sorted(Z, key=lambda x:x[1])
ans=0
flag=True
for k in ct:
    ans+=k[0]
    if ans<=k[1]:
        continue
    else:
        flag=False
        break
print('Yes' if flag==True else 'No')