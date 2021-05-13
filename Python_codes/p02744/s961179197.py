n = int(input())
alphabets = 'abcdefghijkl'
norms = [['a']]
for i in range(1,n):
  rtn = []
  for norm in norms[-1]:
    n_ch = len(set(norm))
    for j in range(n_ch+1):
      rtn.append(norm+alphabets[j])
  norms.append(rtn)
  
for norm in norms[-1]:
  print(norm)