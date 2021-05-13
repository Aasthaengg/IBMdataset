n = int(input())

ans = []

for i in range(n+1):
    ans.append(0)

for x in range(1,101):
    for y in range(1,101):
        for z in range(1,101):
            s = x*x + y*y + z*z
            s += x*y + y*z + z*x
            if (s > n) : continue
            ans[s] += 1

for i in range(1,n+1):
    print(ans[i])
