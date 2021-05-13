def resolve():
    s=[0,0,0,0]
    for i in range(3):
        a,b = map(lambda x: int(x)-1,input().split())
        s[a]+=1
        s[b]+=1
    for i in s:
        if i==3:
            print("NO")
            return
    print("YES")

resolve()