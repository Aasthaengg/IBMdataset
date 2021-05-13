n = int(input())
ans = [0] * n
if n >= 100: N = 100
else: N = n
for x in range(1,N+1):
    for y in range(1, N+1):
        for z in range(1, N+1):
            a =  x**2 + y**2 + z**2 + x*y + y*z + z*x
            if a <= n:
                ans[a-1] += 1
for i in ans: print(i)