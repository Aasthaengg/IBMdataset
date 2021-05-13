dataset = []
wayset = []

while True:
    n, x = input().split()    
    n = int(n)
    x = int(x)
    if n == x == 0:
        break
    dataset.append([n, x])

for x in dataset:
    ways = 0
    for i in range(x[0]):
        for j in range(x[0]):
            for k in range(x[0]):
                if k > j and j > i:
                    if i + j + k + 3 == x[1]:
                        ways += 1
    wayset.append(ways)

for x in wayset:
    print(x)