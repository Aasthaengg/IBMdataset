S = input()
x = len(S)
c = 0
ans = 0
for i in range(x):
  
  if S[i] == 'W':
    
    c += 1
    
    ans += i + 1 - c
    
    
print(ans)