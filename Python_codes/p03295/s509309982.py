n, m = list(map(int, input().split()))
wars = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

sorted_wars = sorted(wars, key=lambda x: x[1])

tail = 0
cnt = 0

for i in range(m):
    if sorted_wars[i][0] >= tail:
        tail = sorted_wars[i][1]
        cnt += 1
print(cnt)