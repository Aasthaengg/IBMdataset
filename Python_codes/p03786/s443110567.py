n = int(input())
a = list(map(int, input().split()))
a.sort()

l = -1
r = n
while r - l > 1:
    m = l + (r-l)//2
    b = a[:]
    b[m] += sum(b[:m])
    flag = 1
    for i in range(m, n-1):
        if b[i+1] <= 2*b[i]:
            b[i+1] += b[i]
        else:
            flag = 0
            break

    if flag == 1:
        r = m
    else:
        l = m


print(n-r)
