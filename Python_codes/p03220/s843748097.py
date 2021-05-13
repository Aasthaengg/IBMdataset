import sys
N = int(input())
T,A = map(int,input().split())
array_hight = list(map(int,input().split()))

min = max(array_hight)
point = ''
for I in array_hight:
    if abs(A - (T - (I * 0.006))) < min:
        min = abs(A - (T - (I * 0.006)))
        point = array_hight.index(I)
print(int(point)+1)