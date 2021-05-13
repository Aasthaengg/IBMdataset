import statistics

while True:
    n = int(input())
    if n == 0:
        break
    else:
        data_set = [int(i) for i in input().split()]
        print(statistics.pstdev(data_set))