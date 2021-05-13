x,y=map(int,input().split())
ans=[x]
while True:
    tmp=ans[-1]*2
    if tmp<=y:
        ans.append(tmp)
    else:
        break
print(len(ans))