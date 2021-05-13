N = int(input())
fact = {}
for p in range(1,N+1):
    pf={}
    m=p
    for i in range(2,int(m**0.5)+1):
        while m%i==0:
            pf[i]=pf.get(i,0)+1
            m//=i
    if m>1:pf[m]=1

    for key,value in pf.items():
        if key in fact.keys():
            fact[key] += value
        else:
            fact[key] = value

L = list(fact.values())
n75 = 0
n25 = 0
n15 = 0
n5 = 0
n3 = 0
n1 = 0
for m in L:
    m += 1
    if m>=75:
        n75+=1
    if m>=25:
        n25+=1
    if m>=15:
        n15+=1
    if m>=5:
        n5+=1
    if m>=3:
        n3+=1
    if m>=1:
        n1+=1

cnt = []
cnt.append(n75)
cnt.append(n25*(n3-1))
cnt.append(n15*(n5-1))
cnt.append(( n5*(n5-1)//2 )*(n3-2))
# print(n1,n3,n5,n15,n25,n75)
# print(cnt)
print(sum(cnt))