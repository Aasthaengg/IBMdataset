n, x = map(int, input().split())
l = list(map(int, input().split()))

cnt = 1
z = 0

for i in range(n):
    z += l[i]
    if z <= x:
        cnt += 1
        
print(cnt)