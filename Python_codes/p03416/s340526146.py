a,b = map(int,input().split())

result = 0
for i in range(a,b+1):
  tar = str(i)
  if tar[0] == tar[4] and tar[1] == tar[3]:
    result += 1
print(result)