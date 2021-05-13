N, Y = map(int, input().split())

ans = [-1, -1, -1]
for i in range(N+1):
    for j in range(N-i+1):
        k = N - (i + j)
        if 10000*i + 5000*j + 1000*k == Y:
            ans = [i, j, k]
            break
    else:
        continue
    break

print(ans[0], ans[1], ans[2])