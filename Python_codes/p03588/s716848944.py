N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

max_a = 0
min_b = -1
for i in range(N):
    a = AB[i][0]
    b = AB[i][1]
    if a > max_a:
        max_a = a
        min_b = b
print(max_a + min_b)
