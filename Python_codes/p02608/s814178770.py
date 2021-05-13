n = int(input())
ans = [0]*n
for x in range(1,101):
    for y in range(1,101):
        for z in range(1,101):
            a = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if a > n: continue
            ans[a-1] += 1
for i in ans: print(i)