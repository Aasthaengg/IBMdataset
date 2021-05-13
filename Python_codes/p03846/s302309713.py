n = int(input())
A = list(map(int, input().split()))
mod = 10**9+7

if n%2 == 1:
    m = (n+1)//2
    l =[0]*m
    for i in range(n):
        if (n-A[i]-1)%2 != 0:
            print(0)
            exit()
        else:
            id = (n-A[i]-1)//2
            l[id] += 1
    #print(l)
    ans = 1
    for i in range(m):
        #print(i, ans)
        if i != m -1:
            if l[i] != 2:
                print(0)
                exit()
            else:
                ans *= l[i]
                ans %= mod
        else:
            if l[i] != 1:
                print(0)
                exit()
            else:
                ans *= l[i]
                ans %= mod
    print(ans)

else:
    m = n//2
    l =[0]*m
    for i in range(n):
        if (n-A[i]-1)%2 != 0:
            print(0)
            exit()
        else:
            id = (n-A[i]-1)//2
            l[id] += 1
    #print(l)
    ans = 1
    for i in range(m):
        #print(i, ans)
        if l[i] != 2:
            print(0)
            exit()
        else:
            ans *= l[i]
            ans %= mod
    print(ans)
