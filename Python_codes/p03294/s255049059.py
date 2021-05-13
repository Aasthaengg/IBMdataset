input()
numbers = tuple(map(int, input().split(' ')))
print(sum([n - 1 for n in numbers]))
