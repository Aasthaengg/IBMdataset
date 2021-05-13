from itertools import*
n,c,*L=map(int,open(0).read().split())
acc=[a-x for x,a in zip(L[::2],accumulate(L[1::2]))]
acc_max=list(accumulate([0]+acc,max))
R=L[::-1]
rev=[a-(c-x) for x,a in zip(R[1::2],accumulate(R[::2]))]
rev_max=list(accumulate([0]+rev,max))
p=max(rev_max[n-i-1]+a-b for i,(a,b) in enumerate(zip(acc,L[::2])))
q=max(acc_max[n-i-1]+a-(c-b) for i,(a,b) in enumerate(zip(rev,R[1::2])))
r=max(0,acc_max[-1],rev_max[-1])
print(max(p,q,r))