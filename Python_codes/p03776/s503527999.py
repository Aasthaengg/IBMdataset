import math

def nCr(n,r):
    return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))

N,A,B = map(int,input().split())

v = list(map(int,input().split()))

minlis = []
maxlis = []

v.sort()

for i in range(N):

    if i < N-A:
        minlis.append(v[i])

    else:
        maxlis.append(v[i])


ave = sum(maxlis) / A
print (ave)


x = min(maxlis)

xinmax = 0
xinmin = 0

for i in minlis:
    if i == x:
        xinmin += 1

for i in maxlis:
    if i == x:
        xinmax += 1

if ave == x and xinmin != 0:

    ans = 0

    for i in range(xinmax + xinmin - A + 1):

        i += A
        if i > B:
            break

        ans += nCr(xinmin+xinmax,i)

    print (ans)

else:

    print (nCr(xinmin+xinmax,xinmax))