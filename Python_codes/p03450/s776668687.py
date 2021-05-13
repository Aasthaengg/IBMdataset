def sol():
    n,m=map(int,input().split())
    t,w={},{}
    p,q=set(),set()
    for i in range(m):
        l,r,d=[int(i) for i in input().split()]
        if l in w: w[l].add((r,d))
        else: w[l]={(r,d)}
        p.add(l)
        q.add(r)
    s=p-q
    chk=set()
    if len(s)==0:
        print(["No","Yes"][m==0])
        exit()
    for i in s:
        chk.add((i,0))
        while len(chk):
            x=chk.pop()
            if x[0] in w:
                for j in w[x[0]]:
                    if (i,j[0]) in t and t[(i,j[0])]!=t[(i,x[0])]+j[1]:
                        print("No")
                        exit()
                    elif (i,j[0]) not in t:
                        #t[(i,j[0])]=t[(i,x[0])]+j[1]
                        t[(i,j[0])]=x[1]+j[1]
                        chk.add((j[0],x[1]+j[1]))
    print("Yes")

if __name__=="__main__":
    sol()
