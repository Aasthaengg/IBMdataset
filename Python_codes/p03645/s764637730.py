n, m = map(int, input().split())

data1 = [0] * (n+1)
data2 = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        data1[b+1] = 1
    if b == n:
        data2[a+1] = 1


for i in range(n+1):
    if data1[i] == 1 and data2[i] == 1:
        print("POSSIBLE")
        exit()

print("IMPOSSIBLE")