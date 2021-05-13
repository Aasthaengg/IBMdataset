N = int(input())
for i in range(1, 9 + 1):
  if N % i == 0 and N / i <= 9:
    result = "Yes"
    break
  else:
    result = "No"
print(result) 