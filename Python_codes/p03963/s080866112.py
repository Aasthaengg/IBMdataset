n,k= map(int,input().split())

if n==1:
    print(k);exit()
print(k*((k-1)**(n-1)))

