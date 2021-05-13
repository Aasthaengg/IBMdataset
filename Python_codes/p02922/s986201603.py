import math
a,b = map(int, input().split())
strips = 0
socket = 1
while socket < b:
    socket = socket-1+a
    strips += 1
print(strips)