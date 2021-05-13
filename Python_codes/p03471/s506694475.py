N, Y = map(int, input().split())


found = False
for i in range(N+1):
    for j in range(N+1):
        k = (Y - (10000*i + 5000*j)) // 1000
        if i + j + k == N and k >= 0:
            print(i, j, k)
            found = True
            break
    if found:
        break

if not found:
    print(-1, -1, -1)