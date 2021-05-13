n = int(input())
mod = int(1e9+7)
cnt = 1

if n == 1:
    print(1)
    exit()

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

fd = dict()
for i in range(2, n+1):
    f = factorization(i)
    for j in f:
        if j[0] not in fd:
            fd[j[0]] = j[1]
        else:
            fd[j[0]] += j[1]
fd = list(fd.values())
for i in fd:
    cnt *= i+1
    cnt %= mod
print(cnt)

