import math

N = int(input())
ans = [0] *(N+1)
a = int(math.sqrt(N)) + 1

for i in range(1,a) :
    for j in range(1,a) :
        for k in range(1,a) :
            n = i**2 + j**2 + k**2 + i*j + i*k + j*k
            if n <= N :
                ans[n] += 1

for m in range(N) :
    print(ans[m+1])


