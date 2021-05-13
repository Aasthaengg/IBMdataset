K=int(input())
if K%2==0:
    print((K//2)**2)
else:
    d = (K-1)//2
    k = (K+1)//2
    print(d*k)