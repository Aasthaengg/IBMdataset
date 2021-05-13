N = input()
ans = 'No'
if N[0] == N[1] and N[1] == N[2]:
  ans = 'Yes'
if N[3] == N[1] and N[1] == N[2]:
  ans = 'Yes'
print(ans)