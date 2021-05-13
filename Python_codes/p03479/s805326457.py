X,Y = map(int,input().split())
ans = 1
for i in range(100):
    X *= 2
    if X > Y:
        break
    ans += 1
print(ans)