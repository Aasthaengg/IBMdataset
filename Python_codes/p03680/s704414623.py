n = int(input())
an = [int(input()) for num in range(n)]

answer = False
count = 1
index = 1
while(True):
  if count > len(an):
    break
  if an[index-1] == 2:
    answer = True
    break
  index = an[index-1]
  count += 1

if answer :
  print(count)
else :
  print(-1)  