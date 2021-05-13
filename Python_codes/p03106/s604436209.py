a,b,k=map(int,input().split())
N=[]
for i in range(1,min(a,b)+1):
    if (a%i==0 and b%i==0):
            N.append(i)
N.reverse()
print(N[k-1])