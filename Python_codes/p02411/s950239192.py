results = []
while True:
    m, f, r = [int(i) for i in input().split()]
    if m == -1 and f == -1 and r == -1:
        break
    if m == -1 or f == -1:
        results.append('F')
    elif m + f >= 80:
        results.append('A')
    elif m + f >= 65:
        results.append('B')
    elif m + f >= 50:
        results.append('C')
    elif m + f >= 30:
        if r >= 50:
            results.append('C')
        else:
            results.append('D')
    else:
        results.append('F')

for result in results:
    print(result)

