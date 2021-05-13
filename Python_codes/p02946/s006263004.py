k, x = map(int, input().split())
xMin = -1000000
xMax =  1000000

ans = list(range(max(x-k+1, xMin), min(x+k, xMax+1)))
for a in ans:
    print(a, end=' ')