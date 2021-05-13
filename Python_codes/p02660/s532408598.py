n=int(input())
p=[]

for i in range(2,int(-(-n**0.5//1))+1) :
    if n%i==0 :
        count=0
        while n%i==0 :
            count+=1
            n//=i
        p.append([i,count])

if n!=1 :
    p.append([n,1])


ans=0
for i in range(len(p)) :
    m=p[i][1]
    j=1
    while m>0 :
        m-=j
        if m>=0 :
            j+=1
            ans+=1

print(ans)