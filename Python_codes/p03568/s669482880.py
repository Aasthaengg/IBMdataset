n = int(input())
even = len([a for a in map(int, input().split()) if a % 2 == 0])
print(3 ** n - 2 ** even)