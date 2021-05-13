N, x = map(int, input().split())
lst = [int(x) for x in input().split()]
total = sum(lst)
for i in range(N - 1):
    if lst[i] + lst[i + 1] > x:
        lst[i + 1] = lst[i + 1] - min(max(lst[i] + lst[i + 1] - x, 0), lst[i + 1])
    if lst[i] + lst[i + 1] > x:
        lst[i] = lst[i] - min(max(lst[i] + lst[i + 1] - x, 0), lst[i])
print(total - sum(lst))
