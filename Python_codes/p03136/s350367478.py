import math
def main():
  n = int(input())
  l = list(map(int,input().split()))
  sum=l[0]
  max=l[0]
  for i in range(1,n):
    sum+=l[i]
    if l[i]>max:
      max=l[i]
  sum-=max
  if sum>max:
    print("Yes")
  else:
    print("No")
main()