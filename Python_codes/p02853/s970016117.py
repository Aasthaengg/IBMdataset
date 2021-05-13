x,y = map(int,input().split())
ans = 0
for i in range(1,4):
    for j in [x,y]:
        if j == i:
            ans += (4-i)*10**5
print(ans+400000 if x*y == 1 else ans)