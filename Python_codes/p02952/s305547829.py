n = int(input())
count = 0
for i in range(1,n+1):
  if 1<=i<=9 or 100<=i<=999 or 10000<=i<=99999:
    count += 1
print(count)