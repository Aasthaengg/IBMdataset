D, T, S = input().split()
sum_price = int(T) * int(S)
if int(D) <= sum_price:
  print("Yes")
else:
  print("No")

