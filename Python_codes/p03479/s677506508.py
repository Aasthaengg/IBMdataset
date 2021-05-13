X,Y = map(int,input().split())
ans = 0
t = 1
while 1:
    if X*t<=Y:
        ans += 1
        t *= 2
    else:break
print(ans)