n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
jewelry = []
for i in range(n):
    if v[i] < c[i]:
        jewelry.append(0)
    else:
        cost = v[i] - c[i]
        jewelry.append(cost)
print(sum(jewelry))