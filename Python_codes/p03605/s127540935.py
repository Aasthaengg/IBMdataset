n = int(input())

m = n%10
l = n // 10

if m==9 or l==9:
    print("Yes")
else:
    print("No")