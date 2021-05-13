n, y = map(int, input().split())
flag = 0
for a in range(n+1):
    s = n-a
    for b in range(s+1):
        c = s-b
        if (a*1000 + b*5000 + c*10000) == y:
            print(c,b,a);    flag = 1
    if flag:
        break
else:
    print(-1,-1,-1)