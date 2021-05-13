from statistics import pstdev

while input() != '0':
    print(pstdev(map(int, input().split())))