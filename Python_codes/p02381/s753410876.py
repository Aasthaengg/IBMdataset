import statistics
while True:
    x = int(input())
    if x == 0:
        break
    else:
        ls = list(map(int, input().split()))
        print("{0:.8f}".format(statistics.pstdev(ls)))