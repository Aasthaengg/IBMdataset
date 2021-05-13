n, k = [int(x) for x in input().split()]
temp_list = sorted([[int(x) for x in input().split()] for _ in range(n)])
ans = 0
for a, b in temp_list:
    k -= b
    if k <= 0:
        ans = a
        break
print(a)