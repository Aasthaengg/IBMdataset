def train():
    n=int(input())
    al=[]
    for _ in range(n):
        a=int(input())
        al.append(a)
    id=0
    ans=1
    for _ in range(n):
        if al[id]==2:
            print(ans)
            return
        else:
            id=(al[id])-1
            ans+=1
    print(-1)
train()