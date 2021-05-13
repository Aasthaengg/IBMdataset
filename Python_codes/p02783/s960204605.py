# 153 A

h, a = map(int, input().split())
num = 0

while h - a >= 0:
    h = h - a 
    num += 1

if h != 0:
    num += 1

print(num)