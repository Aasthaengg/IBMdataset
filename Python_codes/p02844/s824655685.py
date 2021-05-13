n = int(input())
s = input()
ans = 0
lis = [0]*1000
one = [0]*10
two = [0]*100

for i in range(n):
  temp1 = int(s[i])
  if one[temp1]==1:
    continue
  else:
    one[temp1]=1
 
  for j in range(i+1, n):
    temp2 =  int("".join([s[i], s[j]]))
    if two[temp2]==1:
      continue
    else:
      two[temp2]=1
    
    for k in range(j+1, n):
      pin=int("".join([s[i], s[j], s[k]]))
      if lis[pin]==0:
        ans+=1
        lis[pin]=1
print(ans)