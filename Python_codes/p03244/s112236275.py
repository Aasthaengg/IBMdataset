n = int(input())
v = list(map(int,input().split()))
dic1,dic2 = {},{}
c1,c2=0,0
for i in range(0,n,2):
  if v[i] in dic1.keys():
    dic1[v[i]] += 1
  else:
    dic1[v[i]] = 1
  c1 += 1

for i in range(1,n,2):
  if v[i] in dic2.keys():
    dic2[v[i]] += 1
  else:
    dic2[v[i]] = 1
  c2 += 1

dic1 = sorted(dic1.items(), key = lambda x : x[1], reverse=True)
dic2 = sorted(dic2.items(), key = lambda x : x[1], reverse=True)
if len(dic1) == 1:
  dic1.append((0,0))
if len(dic2) == 1:
  dic2.append((0,0))

ans = 0
if dic1[0][0] != dic2[0][0]:
  ans = c1 - dic1[0][1] + c2 - dic2[0][1]
else:
  x = c1 - dic1[0][1] + c2 - dic2[1][1]
  y = c1 - dic1[1][1] + c2 - dic2[0][1]
  ans = min(x,y)

print(ans)