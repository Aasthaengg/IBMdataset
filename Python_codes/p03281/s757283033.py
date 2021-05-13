def factorization(n):
    retlist = []
    tmp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            retlist.append([i, cnt])

    if tmp != 1:
        retlist.append([tmp, 1])

    if retlist == []:
        retlist.append([n, 1])

    return retlist

n = int(input())
ans = 0
for i in range(1,n+1,2):
    d = factorization(i)
    count = 1
    for k,val in d:
        count *= val+1
    if count == 8:
        ans += 1
print(ans)
