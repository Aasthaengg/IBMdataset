import sys
N = int(input())
array = list(map(int,input().split()))
if not (3 <= N <= 10): sys.exit()
if not (min(array) >= 1 and max(array) <= 100): sys.exit()

print('Yes') if max(array) < (sum(array) - max(array)) else print('No')