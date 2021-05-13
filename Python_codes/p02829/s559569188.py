import sys
A = int(input())
B = int(input())
array = [1,2,3]

array.pop(array.index(A))
array.pop(array.index(B))
print(*array)