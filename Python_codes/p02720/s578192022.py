k=int(input())
result = []
def dfs(pos, val):
  result.append(val)

  if pos == 10:
    return
  
  for i in range(-1,2):
    add_num = (val % 10) + i
    if 0 <= add_num <= 9:
      dfs(pos+1, val*10+add_num)

for i in range(1,10):
  dfs(1,i)
result.sort()
print(result[k-1])