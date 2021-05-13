n,m = list(map(int, input().split()))
a = []
b = []
result = []
row_sum = 0

for i in range(n):
    l = list(map(int, input().split()))
    a.append(l)

for i in range(m):
    b.append(int(input()))

for row in a:
    for i,num in enumerate(row):
        row_sum += num * b[i]
    print(row_sum)
    row_sum = 0