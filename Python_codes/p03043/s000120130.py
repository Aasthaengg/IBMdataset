n,k=map(int,input().split())
p=0
for i in range(1,n+1): p+=[1,4/2**len(bin(~-k//i))][i<k]
print(p/n)