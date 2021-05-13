R, D, X = map(int,input().split())
ans = R * X - D
print(ans)
for i in range(9):
    ans = R * ans - D
    print(ans)