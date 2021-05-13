ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

reds = dict()
blues = dict()

n=ni()
for i in range(n):
  s = input()
  if s not in blues:
    blues[s] = 1
  else:
    blues[s]+=1

n = ni()
for i in range(n):
  s = input()
  if s not in reds:
    reds[s] = 1
  else:
    reds[s]+=1


ans=0
for k in blues.keys():
  if k in reds:
    num = blues[k]-reds[k]
    if num>0:
      ans = max(ans,num)
      continue
  else:
    ans = max(ans,blues[k])
  # ans+=blues[k]

print(ans)
