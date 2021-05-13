n = int(input())
a = list(map(int,input().split()))
dict = {}
ans = 0

for i in a:
  if i not in dict:
    dict[i] = 1
  else:
    dict[i] += 1
    
for k,v in dict.items():
  if k > v:
    ans += v
  else:
    ans += v-k
    
print(ans)