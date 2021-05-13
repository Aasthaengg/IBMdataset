N = int(input())
if N == 0:
  print(0); exit()
ans = []
while N !=0:
  #print(ans,N)
  if N%2 == 0:
    ans.append(0)
  else:
    N -= 1
    ans.append(1)
  N//=-2
#print(ans)
ans = reversed(ans)
print(''.join([str(n) for n in ans]))