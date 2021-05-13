n = int(input())
total = 0
for i in range(1, n+1):
    total += i
    if total >= n:
        for j in range(1, i+1):
            if j != total-n:
                print(j)
        exit()
