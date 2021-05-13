import sys
array_no = list(map(int,input().split()))
for I in array_no:
    if not (1 <= I <= 9): sys.exit()

max_first = array_no.pop(array_no.index(max(array_no)))
max_second = array_no.pop(array_no.index(max(array_no)))
print(int(str(max_first)+str(max_second)) + array_no[0])