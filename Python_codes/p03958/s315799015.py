K, T = map(int, input().split())
cake = [int(i) for i in input().split()]

print(max((max(cake) - 1 - (K -  max(cake))), 0))