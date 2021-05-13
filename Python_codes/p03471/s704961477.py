N, Y = map(int, input().split())

l = 0

for i in range(N + 1):
    for j in range(N + 1):
        k = N - i - j
        if 1000*i + 5000*j + 10000*k == Y and k <= N and k >= 0:
            print(k, j, i)
            l = 1
            break
    else:
        continue
    break

if l == 0:
    print("-1 -1 -1")