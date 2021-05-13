n=int(input())
a=int(input())

if n>=500:
    n=n%500

if n<=a:
    print("Yes")
else:
    print("No")