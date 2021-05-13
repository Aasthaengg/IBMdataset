a, b = [int(x) for x in input().split()]
print(sum([1 for i in range(a, b + 1) if i == int(str(i)[::-1])]))