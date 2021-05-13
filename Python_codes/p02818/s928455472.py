a,b,k=map(int,input().split())
k,a=k-min(a,k),a-min(a,k)
k,b=k-min(k,b),b-min(k,b)
print(a,b)