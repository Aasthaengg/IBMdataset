def chkp(P):
    global n, k, w
    i = 0
    for j in range(k):
        s = 0
        while s + w[i] <= P:
            s += w[i]
            i += 1
            if(i == n):
                return n
    return i

def binary_search():
    l = 0
    r = 100000 * 10000
    while r - l > 1:
        c = (l+r) // 2
        v =  chkp(c)
        if(v >= n):
            r = c
        else:
            l = c
    return r

n, k = map(int, input().split())
w = [int(input()) for i in range(n)]
res = binary_search()
print(int(res))
