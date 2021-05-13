red, blue= input().split()
r, b = [int (x) for x in input().split()]
s = input()
if s == red:
    r = r - 1
else:
    b = b - 1
print(r, end=" ")
print(b)
