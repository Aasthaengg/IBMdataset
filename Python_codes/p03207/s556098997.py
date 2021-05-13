import sys
N = int(input())
array = []
for I in range(N): array.append(int(input()))
for J in array:
    if not ( 100 <= J <= 10000 ): sys.exit()
if not ( 2 <= N <= 10 ): sys.exit()

print(max(array)//2 + sum(array) - max(array))