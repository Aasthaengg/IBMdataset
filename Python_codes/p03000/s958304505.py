import sys
N,X = map(int,input().split())
array = list(map(int,input().split()))

count = 1
point = 0
for I in range(len(array)):
    point += array[I]
    if point <= X:
        count += 1
    else:
        break
print(count)