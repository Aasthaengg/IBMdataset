a=[]
while True:
    l=list(input())
    if l[0]=="-":
        break
    else:
        #for shuffle
        m=int(input())
        i=0
        while i<m:
            h=int(input())
            n=0
            while n<h:
                l.append(l[0])
                l.remove(l[0])
                n+=1
            i=i+1
        #for print
        q=1
        Ans=l[0]
        while q<len(l):
            Ans+=l[q]
            q+=1
        a.append(Ans)
for A in a:
    print(A)
