import statistics
while 1:
    n = int(input())
    if n == 0:
        break
    else:
        data = list(map(int, input().split()))
        print(statistics.pstdev(data))