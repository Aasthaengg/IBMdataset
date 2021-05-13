import sys

read = sys.stdin.read
readline = sys.stdin.readline

K, *A = map(int, read().split())
maximum = 2
minimum = 2
for i in A[::-1]:
    if maximum // i - (minimum - 1) // i >= 1:
        maximum = maximum // i * i + i - 1
        minimum = (minimum + i - 1) // i * i
    else:
        print(-1)
        exit()

print(minimum, maximum)
