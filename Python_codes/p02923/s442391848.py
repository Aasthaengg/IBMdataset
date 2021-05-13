input()
towers = list(map(int, input().split()))
#print(towers)
ans = []
count = 0
for x in range(len(towers)-1):
  if towers[x] >= towers[x+1]:
    count+=1
  else:
    ans.append(count)
    count = 0

ans.append(count)

#print(ans)
print(max(ans))