def f(x, y, z):
    return x**2+y**2+z**2+x*y+y*z+z*x
n = int(input())
ans = {}
for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            tmp = f(x, y, z)
            if tmp > n:
                break
            else:
                if tmp not in ans:
                    ans[tmp] = 1
                else:
                    ans[tmp] += 1

for i in range(1, n+1):
    if i in ans:
        print(ans[i])
    else:
        print(0)