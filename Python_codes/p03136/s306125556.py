n = int(input())
lst = list(map(int, input().split()))
print('Yes' if 2 * max(lst) < sum(lst) else 'No')