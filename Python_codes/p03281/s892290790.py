N = int(input())
num=0
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
for i in range(1,N+1):
    ans=1
    if i%2==1:
        a=factorization(i)
        #print(a)
        for u in a:
            ans*=u[1]+1
        if ans==8:
            num+=1
print(num)