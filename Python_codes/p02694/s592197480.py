x=int(input())
c=100
for i in range(1,10**8):
  c=c*101//100
  if c >= x:
    print(i)
    exit()
print("ERROR!")
