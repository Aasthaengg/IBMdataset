K, T = [int(x) for x in input().split()]
a = list([int(x) for x in input().split()])

max_cake = max(a)

if max_cake >= K - max_cake:
    result = max_cake - (K - max_cake) - 1
else:
    result = 0

print(result)
