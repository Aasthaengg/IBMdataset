n,k,*l=map(int,open(0).read().split());l.sort();c,a,M=1,0,10**9+7
for i in range(k-1,n):a+=c*(l[i]-l[~i]);c=c*-~i*pow(i-k+2,M-2,M)%M
print(a%M)