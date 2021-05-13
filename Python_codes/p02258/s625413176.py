_temp = []

size = int(input().rstrip())
for i in range(size):
    try:
        _temp.append(int(input()))
    except EOFError:
        continue

my_max = -20000000000000
my_min = _temp.pop(0)


for val in _temp:
    my_max = max(my_max, (val - my_min))
    my_min = min(my_min, val)

print(my_max)