n = int(input())
L = []
for _ in range(n):
    a,b = map(int,input().split())
    L.append(((a+b),a,b))
L.sort(reverse=True)
ta = 0
ao = 0
for i in range(n):
    if i % 2 == 0:
        ta += L[i][1]
    else:
        ao += L[i][2]
print(ta-ao)