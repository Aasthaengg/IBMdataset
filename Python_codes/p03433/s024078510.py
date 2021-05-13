n = int(input())
a = int(input())
if a == 0:
    print("No" if n % 500 else "Yes")
elif (n % 500) <= a:
    print("Yes")
else:
    print("No")