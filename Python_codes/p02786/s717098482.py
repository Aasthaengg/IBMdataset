H = int(input())

if H==1:
  print(1)
  exit()

i=a=0
while H >= a:
  i += 1
  a = pow(2,i)

# print(H, i,a)
ans = pow(2,i)-1
print(ans)