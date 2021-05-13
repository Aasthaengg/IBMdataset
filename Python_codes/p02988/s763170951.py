n = int(input())
p = list(map(int,input().split()))
ans = 0
for i in range(n):
  if n == i + 2:
    break
  else:
    
    p_com = p[i:i+3]
    sp_com= sorted(p_com)
    if sp_com[1] == p_com[1]:
      ans += 1
      
print(ans)
