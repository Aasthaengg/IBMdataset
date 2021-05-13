n = int(input())
l = [0]*(n+1)
for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            ans = x**2+y**2+z**2+x*y+x*z+y*z
            if(ans>n):
                continue
            l[ans] += 1

print(*l[1:])

