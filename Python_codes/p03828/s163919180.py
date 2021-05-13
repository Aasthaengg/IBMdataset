n = int(input())
mod = 10**9 + 7
dic = {}

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
            
    if temp != 1:
        arr.append([temp, 1])
        
    if arr == []:
        arr.append([n, 1])

    return arr

for i in range(1, n+1):
    a = factorization(i)
    for i in range(len(a)):
        if a[i][0] not in dic:
            dic[a[i][0]] = 1
        else:
            dic[a[i][0]] += a[i][1]

ans = 1
for k in dic.values():
    ans *= k+1
print((ans//2)%mod)