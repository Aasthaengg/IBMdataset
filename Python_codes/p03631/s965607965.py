n = int(input())
a = n//100
b = (n - a*100)//10
c = n - a*100 - b*10
if a == c:
    print("Yes")
else:
    print("No")