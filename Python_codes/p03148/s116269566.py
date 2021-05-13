n,k = map(int,input().split())
l = [tuple(map(int, input().split())) for _ in range(n)]
l.sort(key=lambda x:-x[1])
dic = dict()
tr = list()
curd = 0
curt = 0
for t,d in l[:k]:
  curd += d
  if t not in dic:
    curt += 1
    dic[t] = d
  elif dic[t] < d:
    tr.append(dic[t])
    dic[t] = d
  else:
    tr.append(d)
ans = curt**2 + curd
tr.sort(reverse=True)
for t,d in l[k:]:
  if t in dic: continue
  if not tr: break
  curt += 1
  dic[t] = d
  curd += d - tr.pop()
  cur = curt**2 + curd
  if ans < cur: ans = cur
print(ans)