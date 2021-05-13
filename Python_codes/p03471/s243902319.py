N, Y = map(int, input().split())
flag = False
for x in range(N+1):
    for y in range(N+1):
        z = N - x - y
        ans = 10000*x + 5000*y + 1000*z
        if ans == Y and 0 <= z:
            flag = True
            break
    else:
        continue
    break

if flag:
    print(x, y, z)
else:
    print(-1, -1, -1)
