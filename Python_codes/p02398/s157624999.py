print((lambda a: len([i for i in range(a[0], a[1]+1) if a[2] % i == 0]))(list(map(int, input().split()))))