a,b = map(int, input().split())
s = 1
num = 0
while s < b:
    s += (a-1)
    num += 1
print(num)