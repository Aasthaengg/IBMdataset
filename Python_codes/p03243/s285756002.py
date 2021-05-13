import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

lis = [111, 222, 333, 444, 555, 666, 777, 888, 999]

for num in lis:
    if num >= N:
        print(num)
        exit()