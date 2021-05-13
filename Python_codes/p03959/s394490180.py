N=int(input());*T,=map(int,input().split());*A,=map(int,input().split());a=int(A[0]==T[-1])
for p,q,r,s in zip(T,T[1:],A[1:],A[2:]):
 if(p==q)&(r==s):a=a*min(q,r)%(10**9+7)
 elif(p!=q)&(q>r)|(r!=s)&(q<r):a*=0
print(a)