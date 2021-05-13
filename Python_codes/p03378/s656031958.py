n, m, x = map(int, input().split())
a = list(map(int, input().split()))

go_left = 0
go_right = 0

for i in range(x, n+1):
    if a.count(i) == 1:
        go_right += 1

for j in range(0, x):
    if a.count(j) == 1:
        go_left += 1

print(min(go_left, go_right))
