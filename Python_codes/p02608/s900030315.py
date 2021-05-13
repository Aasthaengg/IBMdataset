n = int(input())

cnt = [set() for i in range(n+1)]

def f(x, y, z):
    return x*x+y*y+z*z+x*y+y*z+x*z

for x in range(1, n+1):
    if f(x,1,1) > n: break
    for y in range(1, n+1):
        if f(x,y,1) > n: break
        for z in range(1, n+1):
            t = f(x,y,z)
            if t > n: break
            cnt[t].add((x,y,z))

for i in range(1, n+1):
    print(len(cnt[i]))