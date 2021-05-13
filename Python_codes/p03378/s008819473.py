n, m, x = (int(i) for i in input().split())
list_a = [int(i) for i in input().split()]
list_toll = []
for i in range(0, n + 1):
    if i in list_a: list_toll.append(1)
    else: list_toll.append(0)
print(min(sum(list_toll[:x]), sum(list_toll[x:])))