d,g=map(int,input().split())

p=[]
c=[]
for i in range(d):
    x,y=map(int,input().split())
    p.append(x)
    c.append(y)

m=100000000000000
for i in range(2**d):
    count=0
    count2=0
    for j in range(d):
        if i&(2**j):
            count+=p[j]*(j+1)*100+c[j]
            count2+=p[j]
    if count>=g and count2<m:
        m=count2
    for j in reversed(range(d)):
        if not(i&(2**j)):
            for k in range(p[j]):
                if count>=g and count2<m:
                    m=count2
                    break
                count+=(j+1)*100
                count2+=1
            break

print(m)

