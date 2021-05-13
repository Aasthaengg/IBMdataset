num = int(input())
val = 0
while num > 0:
    val += num%10
    num //= 10
if val == 1:
    print(10)
else:
    print(val)