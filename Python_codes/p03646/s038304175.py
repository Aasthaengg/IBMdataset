k = int(input())
rest = k % 50
print(50)
lst = [50 + k // 50  if i < rest else 50 + (k // 50 - 1) - rest for i in range(50)]
print(*lst)