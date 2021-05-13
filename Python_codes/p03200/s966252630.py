S=input()
S_list=list(S)
num_B = S.count('W')
count = 0
i = 0
for nb in range(num_B):
  while S_list[i] != 'W': i+=1
  count += i - nb
  S_list[nb],S_list[i]=S_list[i],S_list[nb]
  i+=1
print(count)