a, b= map(int, input().split())
num = abs(abs(a)-abs(b))
 
if a * b < 0:
    num += 1
elif a * b == 0 and a > b:
    num += 1
elif a * b > 0:
    if a < 0 and abs(a) < abs(b):
        num += 2
    elif a > 0 and abs(a) > abs(b):
        num += 2
print(num)