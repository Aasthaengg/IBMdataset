"""
implementation of the Insertion Sort
"""
number_of_input = int(raw_input())

numbers = [int(x) for x in raw_input().split()]

for i in range(1, len(numbers)):
    print " ".join([str(x) for x in numbers])
    target = numbers[i]
    index = i - 1
    while index >= 0 and target < numbers[index]:
        numbers[index + 1] = numbers[index]
        index -= 1
    numbers[index + 1] = target

print " ".join([str(x) for x in numbers])