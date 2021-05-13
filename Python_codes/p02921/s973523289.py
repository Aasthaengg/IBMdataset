days = list(str(input()))
days_real = list(str(input()))
count = 0
for i in range(3):
  if days[i] == days_real[i]:
    count += 1
print(count)