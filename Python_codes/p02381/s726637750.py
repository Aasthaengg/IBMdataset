import statistics
while 1:
    n = input()
    if n == "0":
        break
    a = [int(i) for i in input().split()]
    print(statistics.pstdev(a))