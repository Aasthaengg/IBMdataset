import sys
N = int(sys.stdin.readline().rstrip())
L = list(map(int, sys.stdin.readline().rstrip().split()))
l_max = max(L)
l_sum = sum(L)
if l_max < l_sum - l_max:
    print("Yes")
else:
    print("No")