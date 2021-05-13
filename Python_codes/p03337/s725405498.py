import sys
A,B = map(int,input().split())

if not (-1000 <= A <= 1000 and -1000 <= B <= 1000):
    sys.exit()

result = -1000
if A + B > result:
    result = A + B
if A - B > result:
    result = A - B
if A * B > result:
    result = A * B

print(result)