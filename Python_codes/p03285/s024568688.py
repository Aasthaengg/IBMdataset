n=int(input())
frag='No'
for i in range(n//4+2):
  if (n-4*i)%7==0:
    frag="Yes"
    break
print(frag)