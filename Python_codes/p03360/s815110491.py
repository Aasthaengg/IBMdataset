(*abc,) = map(int, input().split())
print(sum(abc) + max(abc) * ((2 ** int(input())) - 1))