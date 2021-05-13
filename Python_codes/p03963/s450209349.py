from sys import stdin

n, k = [int(x) for x in stdin.readline().rstrip().split()]

count = 0
for i in range(n):
    if i == 0:
        count = k
    elif i == 1:
        count = count * (k - 1)
    else:
        count = count * (k - 1)
print(count)
