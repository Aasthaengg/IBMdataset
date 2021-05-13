N = int(input())

ans = [0]*N
for x in range(1,10**2+1):
    for y in range(1,10**2+1):
        for z in range(1,10**2+1):
            p = x**2+y**2+z**2+x*y+y*z+z*x-1
            if p < N:
                ans[p] += 1

[print(i) for i in ans]
