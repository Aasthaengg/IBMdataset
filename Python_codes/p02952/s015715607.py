n = int(input())
ans = 0
for i in range(0, 3):
    for j in range(1*(100**i), 10*(100**i)):
        if j<=n:
            ans += 1
        else:
            print(ans)
            exit()
print(ans)