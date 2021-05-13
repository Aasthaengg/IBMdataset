def tenka18_d():
    n = int(input())
    if n == 1:
        ans = ['Yes', '2', '1 1', '1 1']
        return print(*ans, sep='\n')
    if n == 2:
        return print('No')

    k = -1
    for i in range(2, int((2*n)**0.5)+2):
        if 2*n % i > 0: continue
        if 2*n // i == i - 1:
            k = i
            break
    if k == -1:
        return print('No')

    l = k-1
    res = [[l] for _ in range(k)]
    for i in range(l):
        s = l*(l+1)//2 - (l-i)*(l-i+1)//2 + 1
        arr = [x for x in range(s, s+l-i)]
        res[i] += arr
        for j in range(l-i):
            res[i+1+j].append(arr[j])

    print('Yes')
    print(k)
    for ln in res:
        print(*ln, sep=' ')

if __name__ == '__main__':
    tenka18_d()