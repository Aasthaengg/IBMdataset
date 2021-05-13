N,K=list(map(int,input().split()))
A=list(map(int,input().split()))
S=sum(A)
facts=set()
for i in range(1,int(S**0.5)+1):
    if S%i==0:
        facts.add(i)
        facts.add(S//i)
for f in sorted(facts,key=lambda x:-x):
    rs = [i%f for i in A]
    rs2=sorted(rs)
    rsr = [f-r for r in rs2]
    if f-rs2[-1]>K and rs2[-1]>K:
        continue
    cum=0
    ruiseki=[0]*(N)
    tmp=0
    for i,a in enumerate(rs2):
        cum+=a
        ruiseki[i]=cum
    for i in range(N-1):
        s_l=ruiseki[i]
        s_h = f*(N-i-1)-(ruiseki[-1]-s_l)
        if max(s_l,s_h)<=K:
            print(f)
            break
    else:
        continue
    break