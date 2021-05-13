import math
n = int(input())
for i in range(n, 0, -1):
    if float.is_integer(math.sqrt(i)) == True:
        print(i)
        exit()