n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i, j in d:
    if i == j:
        cnt += 1
    else:
        cnt = 0
    if cnt == 3:
        print("Yes")
        exit()
print("No")