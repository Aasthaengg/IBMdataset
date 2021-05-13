n = int(input())
tn = n - n%2

edge_num = tn * (tn - 2) // 2
if n % 2 == 1:
    edge_num += n - 1
print(edge_num)

for i in range(tn):
    for j in range(i, tn):
        if i == j or tn - 1 - i == j:
            continue
        print(i+1, j+1)
if n % 2 == 1:
    for i in range(tn):
        print(i+1, n)