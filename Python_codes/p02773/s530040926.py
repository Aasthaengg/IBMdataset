dict={}
for _ in range(int(input())):
  s=input()
  if s not in dict:
    dict[s] = 1
  else:
    dict[s] += 1
dict=sorted(dict.items(),key=lambda x:-x[1])
print(*sorted([dict[i][0] for i in range(len(dict)) if dict[0][1]==dict[i][1]]),sep='\n')