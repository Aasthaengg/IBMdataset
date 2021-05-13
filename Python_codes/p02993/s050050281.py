import sys
arr = list(input())

before = arr[0]
for I in range(1,len(arr)):
    if before == arr[I]: print('Bad');sys.exit()
    before = arr[I]
print('Good')