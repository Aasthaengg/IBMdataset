import statistics

while(1):
    n = int(input())
    if n == 0:
        exit()

    s = [int(i) for i in input().split()]
    print(statistics.pstdev(s))