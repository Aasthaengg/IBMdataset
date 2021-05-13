n, m = map(int, input().split())
cnt = 0
lst = []
for _ in range(n):
    a,b = map(int, input().split())
    lst.append((a,b))
lst.sort()
for val in lst:
    cnt += val[1]
    if cnt >= m:
        print(val[0])
        break