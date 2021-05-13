n,c,k = map(int,input().split())
t = sorted([int(input()) for _ in range(n)])
ans,ppl = 1,1
temp = t[0]
for v in t[1:]:
  if v-temp>k or ppl>=c:
    ans += 1
    ppl = 1
    temp = v
  else:
    ppl += 1
  #print(ans)
print(ans)