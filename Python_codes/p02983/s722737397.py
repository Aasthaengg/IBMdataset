L, R = map(int, input().split())
li = []

if R-L >= 2018:
  ans = 0
else:
  for i in range(L, R+1):
    l = i % 2019
    li.append(l)
  ans = 10000
  for i in range(len(li)-1):
    for j in range(i+1, len(li)):
      ans = min((li[i]*li[j])%2019, ans)
  
print(ans)