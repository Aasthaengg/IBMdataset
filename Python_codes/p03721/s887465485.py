n,k = map(int, input().split())
ab = []
for i in range(n):
    a,b = map(int, input().split())
    ab.append((a,b))
ab.sort()
num = 0
for h in range(n):
    num += ab[h][1]
    if k <= num:
        print(ab[h][0])
        break