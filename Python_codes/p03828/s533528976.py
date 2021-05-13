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
if __name__ == '__main__':
    N = int(input())
    map = dict()
    for n in range(N, 1, -1):
        F = factorization(n)
        for f in F:
            p = f[0]
            e = f[1]
            if f[0] in map:
                map[p] += e
            else:
                map[p] = 0
                map[p] += e
    ans = 1    
    for m in map.values():
        ans *= (m + 1)
    print(ans%(pow(10, 9)+7))