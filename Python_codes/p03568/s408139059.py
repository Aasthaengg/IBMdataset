n = int(input())
a = list(map(int, input().split()))
evens = len(list(filter(lambda x: x % 2 == 0, a)))
print(3 ** n - 2 ** evens)
