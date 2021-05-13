import sys
n = int(input())
array = list(map(int,input().split()))

if not ( 3 <= n <= 20 ): sys.exit()

count = 0
for I in range(n-2):
    if array[I] < array[I+1] < array[I+2]: count += 1
    if array[I] > array[I+1] > array[I+2]: count += 1
print(count)