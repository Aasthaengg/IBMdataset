y = raw_input()
n, x = y.split()
n = int(n)
x = int(x)
co = 0

while n != 0 or x != 0:
    for i in range(1, n-1):
        for j in range(2, n):
            for k in range(3, n+1):
                sum = i + j + k
                if sum == x and i < j and j < k:
                    co += 1
                    break

    print co
    
    y = raw_input()
    n, x = y.split()
    n = int(n)
    x = int(x)
    co = 0