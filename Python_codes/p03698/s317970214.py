from collections import defaultdict 

N = input()
dic = defaultdict(int)
 
for s in N:
  dic[s] += 1
  
  if dic[s] > 1:
    print('no')
    exit()
 
print('yes')