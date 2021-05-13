n=int(input())
mod=10**9+7
a=list(map(int,input().split()))
if n%2==1:
    a.append(0)    
a.sort()
if n%2==1:
    for i in range(1,n+1,2):
        #print(i)
        if a[i]!=(i-1) or a[i-1]!=(i-1):
            print("0")
            exit()
    print(2**((n-1)//2)%mod)
else:
    for i in range(1,n+1,2):
        #print(i)
        if a[i]!=(i) or a[i-1]!=(i):
            print("0")
            exit()
    print(2**(n//2)%mod)
