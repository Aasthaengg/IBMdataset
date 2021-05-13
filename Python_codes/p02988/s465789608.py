n = int(input())
p_list = list(map(int, input().split()))

count = 0
for i in range(n - 2):
  if p_list[i] < p_list[i+1] and p_list[i+1] < p_list[i + 2]:
    count += 1
  elif p_list[i + 2] < p_list[i+1] and p_list[i+1] < p_list[i]: 
    count += 1
  else:
    continue
  
print(count)