line = input()
a, b, c = [int(n) for n in line.split()]
k = int(input())
numbers = [a, b, c]
numbers.sort(reverse=True)
numbers[0] *= 2 ** k
print(sum(numbers))
