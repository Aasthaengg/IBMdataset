import sys
import string
N = int(input())
S = input()
s = list(S)
array = string.ascii_uppercase

for I in s:
    if array.index(I) + N <= 25:
        print(array[array.index(I) + N],end='')
    else:
        print(array[(array.index(I) + N) - 26],end='')