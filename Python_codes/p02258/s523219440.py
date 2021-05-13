n = int(input())
maxi = -1000000000
mini = 1000000000
for i in range(n):
    m = int(input())
    if i > 0:
        if m - mini > maxi:
            maxi = m - mini
    if m < mini:
        mini = m
print(maxi)