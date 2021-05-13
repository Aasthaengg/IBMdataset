x = int(input())
a = int(input())
b = int(input())
tmp = x - a
left = tmp - (tmp // b) * b
print(left)