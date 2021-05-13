n = int(input())
a = list(map(int, input().split()))
ca = [[0 for _ in range(3)]]
for i in range(n):
  if(a[i] == ca[i][0]):
    ca.append([ca[i][0]+1,ca[i][1],ca[i][2]])
  elif(a[i] == ca[i][1]):
    ca.append([ca[i][0],ca[i][1]+1,ca[i][2]])
  else:
    ca.append([ca[i][0],ca[i][1],ca[i][2]+1])
ans = 1
for i in range(n):
  ans = (ans * ca[i].count(a[i])) % 1000000007
print(ans)