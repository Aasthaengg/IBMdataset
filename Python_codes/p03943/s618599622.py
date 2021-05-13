lst = list(map(int, input().split()))
lst = sorted(lst)
print('Yes' if lst[0] + lst[1] == lst[2] else 'No')