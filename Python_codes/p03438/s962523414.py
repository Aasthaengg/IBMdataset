import sys
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
plus, minus = 0, 0

if n == 1:
    if a[0] <= b[0]:
        print('Yes')
    else:
        print('No')
    sys.exit()

for i, j in zip(a, b):
    num = j-i
    if num >= 0:
        plus += num//2
    else:
        minus -= num
        
if plus >= minus:
    print('Yes')
else:
    print('No')
