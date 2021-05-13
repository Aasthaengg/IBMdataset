from statistics import pstdev

while True:
    n = input()
    if n == '0':
        break
    print(pstdev(map(int, input().split())))