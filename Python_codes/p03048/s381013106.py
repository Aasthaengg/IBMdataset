r,g,b,n = map(int,input().split(' '))
A = [r,g,b]
A.sort()
r,g,b = A[2], A[1], A[0]
rmax, gmax = n//r, n//g
count = 0
i = 0
while i <= rmax:
    j = 0
    if g == 1:
        count += (n-i*r)+1
        j += 30000
    while (n-i*r-j*g) >= 0:
        if (n-i*r-j*g)%b == 0:
            count += 1
        j += 1
    i += 1
print(count)