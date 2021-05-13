import math
def main():
  n=int(input())
  p = list(map(int,input().split()))
  first=-1
  last=-1
  
  for i in range(0,n-1):
    if p[i]>p[i+1]:
      first=i
      break
  for i in reversed(range(1,n)):
    if p[i]<p[i-1]:
      last=i
      break
  
  if first!=-1 and last!=-1:
    tmp=p[first]
    p[first]=p[last]
    p[last]=tmp

  for i in range(0,n-1):
    if p[i]>p[i+1]:
      print("NO")
      break
    if i==n-2:
      print("YES")  
main()