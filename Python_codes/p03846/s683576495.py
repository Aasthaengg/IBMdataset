mod = 1000000007
    
n=int(input())

t = list(map(int,input().split()))

if n%2==0:
    memo = [0]*n
    for i in t:
        memo[i] += 1
    for j in range(n):
        if j%2==1 and memo[j] != 2:
            print(0)
            exit()
    print((2**(n//2))%mod)  
else:
    memo = [0]*n
    for i in t:
        memo[i] += 1
    if memo[0] != 1:
        print(0)
        exit()
    memo[0]+=1
    for j in range(n):
        if j%2==0 and memo[j] != 2:
            print(0)
            exit()
    print((2**((n-1)//2))%mod) 