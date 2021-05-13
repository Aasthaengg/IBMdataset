N,x,*a = map(int, open(0).read().split())
temp = 0
ans = 0
for c in a:
    t1 = temp
    temp += c
    if temp > x:
        ans += temp - x
        temp = x - t1
    else:
        temp -= t1
print(ans)