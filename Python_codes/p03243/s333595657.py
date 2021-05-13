from math import ceil

n = int(input())
if n%111 == 0:
    print(n)
else:
    print(111*ceil(n/111))