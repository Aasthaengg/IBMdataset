n = int(input())
arr = [1]*(n+1)
mod = 10**9+7
def factorization(n):
    global arr
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr[i] += cnt%mod

    if temp!=1:
        arr[temp] += 1
        arr[temp] %= mod

    if arr==[]:
        arr[n] += 1
        arr[n] %= mod


for i in range(1,n+1):
    factorization(i)

#print(arr)

anslist = [0]*(n+1)
anslist[1] = arr[1]%mod
for i in range(2,n+1):
    anslist[i] = anslist[i-1]*arr[i]
print(anslist[n]%mod)