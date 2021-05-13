n, m = map(int, input().split())
ml, mr = 0, n
for i in range(m):
    l, r = map(lambda x: int(x) - 1, input().split())
    ml = max(ml, l)
    mr = min(mr, r)
print(max(0, mr - ml + 1))
