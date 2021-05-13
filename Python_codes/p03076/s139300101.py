lis = []
rank1 = []
for i in range(5):
  lis.append(input())
  rank1.append( 10 if lis[-1][-1] == "0" else int(lis[-1][-1]))

min_index = rank1.index(min(rank1))
  
ans = 0
for i in range(5):
  if i == min_index:
    continue
  ans = (ans + int(lis[i]) + 9)//10*10
ans += int(lis[min_index])

print(ans)

