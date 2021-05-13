m=int(input())
for i in range(0, 11):
  if i*1000 < m <= (i+1)*1000:
    m=(i+1)*1000 - m
print(m)
