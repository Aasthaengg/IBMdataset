n = int(input())

lis = [2, 1]

while len(lis) <= n:
    lis.append(lis[-1] + lis[-2])

print(lis[-1])