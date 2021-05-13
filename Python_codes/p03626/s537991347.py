N = int(input())
DS = list(input())
i = 0
DC = []
while i<N:
  cnt = DS.count(DS[i])
  DC.append(cnt)
  i += cnt

ans = 3 * DC[0]
for i in range(1,len(DC)):
  if DC[i-1]==1:
    ans = (ans * 2)% 1000000007
  elif DC[i]==2:
    ans = (ans * 3)% 1000000007
print(ans)