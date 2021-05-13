n, m = list(map(int, input().split()))

list = [list(map(int, input().split())) for x in range(m)]

ans = [1]*n

s = 0
m = n

for i in list:
    if i[0] > s:
        s = i[0]
    if i[1] < m:
        m = i[1]
if m>=s:
    print(m-s+1)
else:
    print(0)