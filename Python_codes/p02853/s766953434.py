x, y = map(int,input().split())
ans = 400000 if x == y ==1 else 0

for i in [x,y]:
    if i > 3:
        continue
    ans += (4-i)*100000
print(ans)
