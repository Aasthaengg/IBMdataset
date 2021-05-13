x = int(input())
a = x % 11
b = x // 11
 
if a == 0:
    c = 0
elif a <= 6:
    c = 1
else:
    c = 2
 
print(b * 2 + c)