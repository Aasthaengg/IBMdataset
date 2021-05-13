def solve(hajime, ima, wa):
  for i in range(10):
    #print("hajime : "+str(hajime))
    #print("ima : "+str(ima))
    #print("wa : " + str(wa))
    if i == 1 and wa + c[ima][i] < toone[hajime]:
      toone[hajime] = wa + c[ima][i]
    elif wa + c[ima][i] < toone[hajime] and i != ima:
      solve(hajime, i, wa+c[ima][i])
  return
      
    


h,w = list(map(int, input().split()))
c = [list(map(int, input().split())) for i in range(10)]
a = [list(map(int, input().split())) for i in range(h)]
toone=[10**4]*10
toone[1]=0

for i in range(10):
  if i != 1:
    solve(i, i, 0)

#print(toone)
ans = 0
for i in range(h):
  for j in range(w):
    if a[i][j] != -1:
      ans += toone[a[i][j]]
print(ans)