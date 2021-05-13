def main(n):
  s=0
  if n%10==2:
    s+=1
  if (n%100)//10==2:
    s+=1
  if (n%1000)//100==2:
    s+=1
  if n>=2000 and n<=2999:
    s+=1
  return s
n=int(input())
print(main(n))