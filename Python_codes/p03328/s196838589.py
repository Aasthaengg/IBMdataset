a, b = map(int, input().split())

k = (b-a) - 1
print(int(k*(k+1)/2 - a))