N = int(input())
S1 = str(input())
S2 = str(input())
mod = 10 ** 9 + 7

queue = [0, 1, 2]
ans = 1
p = 0
for i in range(N):
  if p <= 1:
    if S1[i] == S2[i]:
      if i == 0:
        ans *= 3
      else:
        if p == 0:
          ans *= 2
        else:
          ans = ans
      p = 0
    else:
      if i == 0:
        ans *= 6
      else:
        if p == 0:
          ans *= 2
        else:
          ans *= 3 
      p = 2
  else:
    p -= 1
  ans = ans % mod  
      
print(ans)      
      
    
  



