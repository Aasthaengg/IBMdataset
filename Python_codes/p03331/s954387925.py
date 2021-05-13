n = int(input())
candi = []
for i in range(1,int(n/2+1)):
  j = n - i
  candi.append([i,j])

#candi = [[2, 13], [3, 12], [4, 11], [5, 10], [6, 9], [7, 8]]

ans = 0
for a,b in candi:
  count = 0
  a = str(a)
  b = str(b)
  for i in a:
    count += int(i)
  for i in b:
    count += int(i)
  if ans == 0 :
    ans = count
  ans = min(ans,count)

print(ans)