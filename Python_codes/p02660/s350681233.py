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

N = int(input())

if N == 1:
    print("0")
    exit()

factors = factorization(N)

ans = 0
for factor in factors:
    num = factor[1]
    x = 1
    for i in range(num+1):
        if i**2 + i > 2*num:
            x = i-1
            break
#    print(num,x)                                                                                      
    ans += x

print(ans)
