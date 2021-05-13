import sys

read = sys.stdin.read
readline = sys.stdin.readline

K, *A = map(int, read().split())
maximum = 2
minimum = 2
for i in A[::-1]:
    if i > maximum:
        print(-1)
        exit()
    if i >= minimum:
        new_minimum = i
    else:
        new_minimum = (minimum + i - 1) // i * i
    new_maximum = maximum // i * i + i - 1
    if minimum <= new_minimum <= new_maximum and maximum <= new_maximum:
        minimum, maximum = new_minimum, new_maximum
    else:
        print(-1)
        exit()

print(minimum, maximum)
