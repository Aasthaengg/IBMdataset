k,a,b = map(int,input().split())

if a > b:
    print(1+k)
    exit()
kk = k
kk -= a - 1
ans = a + (kk // 2) * (b - a) + (kk % 2)

print(max(ans, 1+k))
