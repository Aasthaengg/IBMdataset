n = int(input())
shinamono = []
for i in range(n):
    p = int(input())
    shinamono.append(p)
shinamono.sort()
ans = shinamono[-1]//2
for i in range(n-1):
    ans += shinamono[i]
print(ans)
