s = int(input())
x1 = 10**9
x2 = 1
def ceil(a, b):
   return a // b + (a % b > 0)

y2 = ceil(s, x1)
y1 = 10**9 - s % 10**9
if y1 == 10**9:
    y1 = 0
print(0)
print(0)
print(x1)
print(y1)
print(x2)
print(y2)