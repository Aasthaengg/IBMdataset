N = int(input())
xxx = [111, 222, 333, 444, 555, 666, 777, 888, 999]
for i in range(N, 1000):
    if i in xxx:
        print(i)
        exit()
