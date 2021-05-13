x = int(input())

ans = 0
for i in range(x+1):
    total = i*(i+1)/2
    if total >= x:
       ans = i
       break
   
print(ans)