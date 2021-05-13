num = int(input())
lst = []
lst2 = []
while num > 0:
    lst.append(num%10)
    lst2.append(num%10)
    num //= 10
lst2.reverse()
if lst == lst2:
  print("Yes")
else:
  print("No")