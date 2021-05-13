from collections import Counter
H, W = map(int,input().split())
d = Counter()
for _ in range(H):
  d.update(list(input()))

# check palindrome
def main():
  num1 = (H*W) % 2 
  num2 = (W % 2)*H//2 + (H % 2)*W//2
  num4 = ((H*W) - num1 - num2*2)//4
  #print(num1,num2,num4)

  check1 = sum([val % 2 for key,val in d.items()])
  #print(check1)
  if check1 != num1:
    return False
  
  check4 = 0
  for key,val in d.items():
    if val >= 4:
      deduct = min(num4-check4,val//4)
      d[key] = val - deduct*4
      check4 += deduct
      
      if check4 == num4:
        break
    
  #print(check4)
  if check4 != num4:
    return False
  
  check2 = sum([val//2 for key,val in d.items()])
  #print(check2)
  if check2 != num2:
    return False
      
  return True
      
  
ans = main()
if ans:
  print("Yes")
else:
  print("No")