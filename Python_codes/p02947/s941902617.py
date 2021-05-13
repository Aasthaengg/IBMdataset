N = int(input())
Dic = {}
ans = 0
for _ in range(N):
  st = input()
  st=''.join(sorted(st))
  if st not in Dic:
    Dic[st]=0
  else:
    Dic[st]+=1
    ans+=Dic[st]
print(ans)