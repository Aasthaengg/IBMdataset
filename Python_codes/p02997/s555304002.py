n, k = map(int, input().split())

maxi = (n-1)*(n-2)/2
if k > maxi:
    print(-1)
    exit()

nokori = int(maxi - k)
print(nokori + n-1)
for i in range(1, n):
    print(i, n)

for i in range(1, n):
    if nokori == 0: break
    for j in range(i+1, n):
        print(i, j)
        nokori -= 1
        if nokori == 0: break