import sys

n=int(input())
a=sorted([int(x) for x in input().split()])
for i in range(n-1):
  if a[i]==a[i+1]:
    print("NO")
    sys.exit()
print("YES")