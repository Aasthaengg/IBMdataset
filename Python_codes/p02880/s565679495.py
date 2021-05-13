n = int(input())
for i in range(1,10):
  if 1<=n/i and n/i<=9 and n%i==0:
    print("Yes")
    exit()
print("No")