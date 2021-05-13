# ABC 075: A – One out of Three
numbers = [int(s) for s in input().split()]
if numbers.count(numbers[0]) == 1:
    print(numbers[0])
elif numbers.count(numbers[1]) == 1:
    print(numbers[1])
else:
    print(numbers[2])