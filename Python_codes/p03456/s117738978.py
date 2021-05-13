s = int(''.join(input().split()))

result = "No"
for x in range(1000):
  if x ** 2 == s:
    result = "Yes"
print(result)