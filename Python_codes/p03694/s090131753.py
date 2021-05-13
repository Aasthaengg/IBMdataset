n = int(input())
array = sorted([int(item) for item in input().split()][:n])
print(array[len(array) - 1] - array[0])
