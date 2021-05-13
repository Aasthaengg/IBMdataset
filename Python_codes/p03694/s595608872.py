import sys
N = int(input())
int_array = list(map(int,input().split()))

if N < 0 or N > 100:
    sys.exit()
if not len(int_array) == N:
    sys.exit()
if max(int_array) > 1000 or min(int_array) < 0:
    sys.exit()

print(max(int_array) - min(int_array))