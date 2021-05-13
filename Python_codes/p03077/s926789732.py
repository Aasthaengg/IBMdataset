# input
N = int(input())

Cap = []
append = Cap.append
for i in range(5):
    append(int(input()))

# check
total = 0
citys = [N] + ([0] * 5)

bottleneck = min(Cap)
print((N + bottleneck - 1) // bottleneck + 4)