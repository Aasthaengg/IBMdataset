import itertools

N = int(input())
S = input()

counter = 0
for a,b,c in itertools.product(range(10), repeat=3):
  
  a_ind = S.find(str(a))
  if a_ind==-1:
    continue
  else:
    b_ind = S[a_ind+1:].find(str(b))
    if b_ind==-1:
      continue
    else:
      c_ind = S[a_ind+1+b_ind+1:].find(str(c))
      if c_ind==-1:
        continue
      else:
        counter += 1
        # print(a_ind,b_ind,c_ind)
        
print(counter)