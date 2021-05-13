import sys

[num, values] = sys.stdin.readlines()
values = [int(x) for x in values.split()]

min_value = 999999999999
max_value = -999999999999
total_value = 0

for value in values:
    if value < min_value:
        min_value = value
    if max_value < value:
        max_value = value

    total_value += value

print("{0} {1} {2}".format(min_value, max_value, total_value))