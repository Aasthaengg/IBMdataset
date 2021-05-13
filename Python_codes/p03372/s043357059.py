n,c,*t=map(int,open(0).read().split())
X=t[::2];V=t[1::2]
def s(X,v):
 V=[0];X=[0]+X;r=[0];l=[0]*-~n
 for i in v:V+=V[-1]+i,
 for i in range(n):r+=V[i+1]-2*X[i+1],;l[n-i-1]=max(l[n-i],V[n]-V[n-i-1]-(c-X[n-i]))
 return [i+j for i,j in zip(r,l)]
print(max(s([c-i for i in X[::-1]],V[::-1])+s(X,V)))