n, k = [int(x) for x in input().split()]
lst = list(map(int, input().split()))

lst = sorted(lst)
print(sum(lst[:k]))
