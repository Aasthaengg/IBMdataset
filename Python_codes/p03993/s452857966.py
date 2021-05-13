n,*a=map(int,open(0).read().split())
print(sum(i+1==a[a[i]-1] for i in range(n))//2)