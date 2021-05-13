N,W = map(int,input().split())
tmpv = [[] for _ in range(4)]
w1 = None
for i in range(N):
    tw, tv = map(int,input().split())
    if i==0:
        w1 = tw
        tmpv[0].append(tv)
    else:
        tmpv[tw-w1].append(tv)

v = []
for tv in tmpv:
    v.append(sorted(tv, reverse=True)+[0])
    
ans = 0
for i in range(len(v[0])):
  for j in range(len(v[1])):
    for k in range(len(v[2])):
      for l in range(len(v[3])):
        tw = w1*i+(w1+1)*j+(w1+2)*k+(w1+3)*l
        tv = sum(v[0][:i]) + sum(v[1][:j]) + sum(v[2][:k]) + sum(v[3][:l])
        if tw<=W:
          ans = max(ans, tv)
print(ans)