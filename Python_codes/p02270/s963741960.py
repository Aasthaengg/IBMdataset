n,k=map(int, input("").split(" "))
w=[]
for i in range(n):
    w.append(int(input("")))
s=sum(w)
m=max(w)
while s>m:
    a=0
    b=0
    tmp=int((s+m)/2)
    for i in w:
        a+=i
        if a>tmp:
            a=i
            b+=1
    if b>=k:
        m=tmp+1
    else:
        s=tmp
print(m)
