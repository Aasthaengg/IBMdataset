def prime(n):
    if n > 1:  
        for i in range(2, n): 
            if (n % i) == 0: 
                return False
                break
        else: 
            return True 
    else: 
        return False
n = int(input())
c = 1
ans = []
for i in range(n):
  flag = True
  while flag:
    val = prime((c*5)+1)
    if val:
      ans.append((c*5)+1)
      flag = False
    c+=1
print(*ans)