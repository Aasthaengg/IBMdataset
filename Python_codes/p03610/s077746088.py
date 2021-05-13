N = input()
NN = list(N)
N_l = len(N)

ans = []

for i in range(N_l):
  if i % 2 == 0:
    ans.append(NN[i])
  else:
    pass
    
print(''.join(ans))