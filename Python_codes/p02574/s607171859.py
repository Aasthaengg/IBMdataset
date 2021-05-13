import math
N = int(input())
A = list(map(int, input().split()))
ans1 = "pairwise coprime"
ans2 = "setwise coprime"
ans3 = "not coprime"

a = math.gcd(A[0], A[1])
for i in range(2, N):
    a = math.gcd(a, A[i])

if a==1:
    b = True
    l = [0]*(10**6+1)
    x = [0]*(10**6+1)
    x[0]=1
    x[1]=1
    for i in range(2, 10**6+1):
        if x[i]==0:
            for j in range(i, 10**6+1, i):
                x[j]=i

    for y in A:
        s=set()
        if y==1:
            continue
        elif y==x[y]:
            s |= {y}        #素因数のリスト
        else:
            while y!=x[y]: #素数になるまで
                s|={x[y]}  
                y//=x[y]
                if y==x[y]:
                    s|={x[y]}
                    break
        for i in s:
            l[i]+=1
            if l[i]>=2:
                b=False
                break
                
        
    if b:
        print(ans1)
    else:
        print(ans2)
        
        
    
else:
    print(ans3)

