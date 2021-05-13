a, b = map(int, input().split())
c = list(map(int, input().split()[:b]))
e = sum(c)
if a<e:
    print(-1)
else:
    print(a-e)