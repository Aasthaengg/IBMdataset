while True:
    data = input().split()
    n = int(data[0])
    x = int(data[1])
    if n == 0 and x ==0:
        break
    count = 0
    for i in range(1,n-1):
        for j in range(i+1,n):
            for k in range(j+1,n+1):
                if i != j and j != k and i != k:
                    c = i + j + k
                    if c == x:
                        count += 1
    print(count)