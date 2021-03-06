def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
import fractions
A,B = map(int,input().split())
ans = factorization(fractions.gcd(A,B))
if ans[0][0] == 1:
    print(len(ans))
else:
    print(len(ans)+1)