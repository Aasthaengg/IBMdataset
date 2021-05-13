n = int(input())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
a.reverse()
b.reverse()

ans = 0
for i in range(n):
    ai = a[i]+ans
    bi = b[i]
    if ai%bi != 0:
       ans += bi-ai%bi
print(ans)
