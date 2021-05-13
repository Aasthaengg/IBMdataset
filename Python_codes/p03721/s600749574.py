n,k = map(int,input().split())
dict = {}
ans = 0

for i in range(n):
  a,b = map(int,input().split())
  if a not in dict:
    dict[a] = b
  else:
    dict[a] += b
    
dic = sorted(dict.items())


for key,v in dic:
  ans += v
  if ans >= k:
    print(key)
    exit()