numbers = [int(x) for x in input().split()]
numbers.sort(reverse=True)

print(10 * numbers[0] + numbers[1] + numbers[2])