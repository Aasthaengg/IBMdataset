ABC = list(input().split())
print([x for x in set(ABC) if ABC.count(x) == 1][0])