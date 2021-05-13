k,x=map(int,input().split())
a=[str(x+i) for i in range(-k+1,k) if x+i>=-1000000 and x+i<=1000000]
print(" ".join(a))