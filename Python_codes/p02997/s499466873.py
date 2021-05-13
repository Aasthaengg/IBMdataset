n, k = map(int, input().split())

remain = (n-1)*(n-2)//2 - k
if remain < 0:
    print(-1)
    exit()

m = n-1 + remain
print(m)
for i in range(1, n):
    print(1, i+1)

for i in range(1, n):
    for j in range(i+1, n):
        if remain > 0:
            print(i+1, j+1)
            remain -= 1
        else:
            exit()