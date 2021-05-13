x,y=map(int,input().split())
ans=[x]
tmp=x
while tmp<y:
    if tmp*2<=y:
        ans.append(tmp)
        tmp=tmp*2
    else:
        break
print(len(ans))