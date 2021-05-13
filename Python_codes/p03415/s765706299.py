c = [list(input()) for _ in range(3)]

ans = []
for i in range(3):
  ans.append(c[i][i])
  
joi = ''.join(ans)
print(joi)
