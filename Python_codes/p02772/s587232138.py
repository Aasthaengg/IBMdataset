import sys

n=int(input())
a=[int(x) for x in input().split()]
for i in range(n):
  if a[i]%2==0 and a[i]%3!=0 and a[i]%5!=0:
    print("DENIED")
    sys.exit()
print("APPROVED")    