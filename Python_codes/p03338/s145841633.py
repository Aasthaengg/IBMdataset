import math
def main():
  n = int(input())
  s = input()
  ans=0
  for i in range(0,n):
    sum=0
    x=s[:i+1]
    y=s[i+1:]
    while len(x)>0:
      if x[0] in y :
        sum+=1
      x=x.replace(x[0],'')
    if sum>ans:
      ans=sum
  print(ans)
main()