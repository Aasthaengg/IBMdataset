def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


n, p = map(int,input().split())
a = list(map(int,input().split()))

even=0
odd=0
for i in a:
    if i%2 == 0:
        even+=1
    else:
        odd+=1
ans = 0
if p == 0:
    evens = 0
    i = 1
    while(i <= even):
        evens += cmb(even, i)

        i+=1

    ans += 1<<even
    i = 2
    while(i <= odd):
        ans += cmb(odd, i) + cmb(odd, i)*evens
        i+=2

    print(ans)

else:
    evens = 0
    i = 1
    while(i <= even):
        evens += cmb(even, i)

        i+=1

    i = 1
    while(i <= odd):
        ans += cmb(odd, i) + cmb(odd, i)*evens

        i+=2
    print(ans)