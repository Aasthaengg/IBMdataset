import sys

K = int(input())
A, B = map(int, input().split())

for i in range(1, 1001):
    if A <= i * K and i * K <= B:
        print("OK")
        sys.exit()
        
print("NG")