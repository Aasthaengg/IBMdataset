n=int(input())
lis=[int(input()) for i in range(n)]
for num in lis:
  if num % 2==1:
    print("first")
    exit()
print("second")