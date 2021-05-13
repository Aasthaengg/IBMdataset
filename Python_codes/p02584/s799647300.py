x,k,d=map(int,input().split())
x=abs(x)
i=min(x//d,k) if (k-x//d)%2==0 else min(x//d+1,k)
print(abs(x-d*i))