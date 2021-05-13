X,Y = map(int,input().split())
ans = 0
for i in range(Y):
    if X <= Y:
        ans += 1
        X *= 2
    else:
        break
print(ans)