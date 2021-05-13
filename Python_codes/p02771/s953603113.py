import sys
array = list(map(int,input().split()))
set_array = set(array)

if not ( 1 <= min(array) and max(array) <= 9 ): sys.exit()

print('Yes') if len(set_array) == 2 else print('No')