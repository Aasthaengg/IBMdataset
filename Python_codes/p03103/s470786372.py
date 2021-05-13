n, m = map(int, input().split())
ab = []
for i in range(n):
    AB = list(map(int, input().split()))
    ab.append(AB)
x = 0
val = 0
ab.sort(key=lambda x:x[0])
for i in range(n):
    x += ab[i][1]
    val += ab[i][0]*ab[i][1]
    if x < m:
        continue
    else:
        val = val - ab[i][0]*(x - m)
        break
print(val)