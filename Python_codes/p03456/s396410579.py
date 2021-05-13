a, b = map(int, input().split())

x = len(str(b))
now = b + a * (10 ** x)
#print(now)
for i in range(500):
  if i * i == now:
    print("Yes")
    quit()
    
print("No")
  
           
           
           




