n=int(input())
if n==1:
    print(0)
else:
    pf={}
    m=n
    for i in range(2,int(m**0.5)+1):
        while m%i==0:
            pf[i]=pf.get(i,0)+1
            m//=i
    if m>1:pf[m]=1
    ans=[]
    m=0
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            m=n//i-1
            if n%m==i and n//m==i:
                ans.append(m)

    #print(int(n**0.5))
    print(sum(ans))