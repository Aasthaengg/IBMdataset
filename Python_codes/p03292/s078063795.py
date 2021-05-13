values = sorted(list(map(int, input().split(' '))))

print(abs(values[1] - values[0]) + abs(values[1] - values[2]))

