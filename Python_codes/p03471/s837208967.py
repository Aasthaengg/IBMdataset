n, y = map(int, input().split())

rem = 0
for i in range(y//10000 +1):
    rem = y-10000*i
    for j in range(rem//5000 + 1):
        k = (rem - 5000*j) // 1000
        if (i + j+ k) == n:
            print(i, j, k)
            break
    else:
        continue
    break
else:
    print(-1, -1, -1)