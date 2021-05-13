N = int(input())
h = list(map(int, input().split()))

mx = max(h)

h_list = [[0 for _ in range(mx)] for _ in range(N)]

for i in range(N):
    for j in range(h[i]):
        h_list[i][j] = 1

# print(h_list)
res = 0

for h in range(mx):
    i = 0
    while i < N:
        if h_list[i][h] == 0:
            i += 1
        else:
            res += 1
            while(i < N and h_list[i][h] == 1):
                i += 1
print(res)
