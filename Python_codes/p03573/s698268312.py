import sys
array = list(map(int,input().split()))

if not (-100 <= array[0] <= 100 and -100 <= array[1] <= 100 and -100 <= array[2] <= 100):
    sys.exit()

for num in array:
    if array.count(num) == 1:
        print(num)
