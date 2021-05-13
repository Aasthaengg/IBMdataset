info=[]
for _ in range(6):
  info.append(int(input()))
from math import ceil
ans=4+ceil(info[0]/min(info[1:]))
print(ans)