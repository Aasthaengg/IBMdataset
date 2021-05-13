n = int(input())
al = []
bl = []
for _ in range(n):
    a, b = map(int, input().split())
    al.append(a)
    bl.append(b)
ans = max(al) + bl[al.index(max(al))]
print(ans)
