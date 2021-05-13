ans = 0
num = int(input())

while(1):
  if num>=3:
    ans += 1
    num -= 3
  else:
    break
    
print(ans)