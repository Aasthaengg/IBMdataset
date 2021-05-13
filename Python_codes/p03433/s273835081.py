n = int(input())
a = int(input())
while n >= 500:
    n -= 500
if n <= a:
    print("Yes")
else:
    print("No")