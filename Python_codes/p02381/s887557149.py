from statistics import pstdev
while True:
    data_count = int(input())
    if data_count == 0:
        break
    print(pstdev(map(int, input().split())))
