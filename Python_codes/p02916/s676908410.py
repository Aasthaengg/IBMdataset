N=int(input())
a=input()
a_=a__=[int(i) for i in a.split()]
b=input()
b_=b__=[int(i) for i in b.split()]
c=input()
c_=c__=[int(i) for i in c.split()]
sat=0
first=a_[0]-1
sat=sat+b_[first]
for x in a_:
    if x>N:
        a_.remove(x)
for x in b_:
    if x<1 or x>50:
        b__=b_.remove(x)
for x in c_:
    if x<1 or x>50:
        c__=c_.remove(x)
a__=list(dict.fromkeys(a_))
if len(a__) ==len(a_) and len(c__)==len(c_) and len(b__)==len(b_) and 2<=N<=50:
    for x in range(1,N):
        if a_[x]==1+a_[x-1]:
            sat=sat+b_[(a_[x])-1]+c_[(a_[x])-2]
        else:
            sat=sat+b_[(a_[x])-1]
    if sat!=0:
        print(sat)