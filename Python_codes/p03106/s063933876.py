def main():
  a,b,k = list(map(int,input().split()))
  loop=0
  if a<b:
    loop=a
  else:
    loop=b
  now=0
  for i in reversed(range(1,loop+1)):
    if a%i==0 and b%i==0:
      now+=1
      if now==k:
        print(i)
        break
main()