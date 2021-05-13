N = int(input())
count=0
for i in range(1,N+1):
  if 1 <= i <= 9:
    count+=1
  elif 100 <= i <= 999:
    count+=1
  elif 10000 <= i <= 99999:
    count+=1
print(count)