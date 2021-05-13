dict={}
for _ in range(int(input())):
  s=''.join(sorted(input()))
  if s not in dict: dict[s]=1
  else: dict[s]+=1
print(sum([i*(i-1)//2 for i in dict.values()]))