s = list(input())
#d = {}
#for si in s:
#  if si in d:
#    d[si] += 1
#  else:
#    d[si] = 1
#mx = 0
#for k,v in d.items():
#  if v > mx:
#    mx = v
#t = []
#for k,v in d.items():
#  if v == mx:
#    t.append(k)
t = set(s)
#print(t)

s = ''.join(s)
ans = 101
for ti in t:
  s1 = s
  cnt = 0
  while(s1.count(ti) != len(s1)):
    #print(ti,cnt,s1)
    s2 = ''
    for i in range(len(s1)-1):
      if s1[i] == ti or s1[i+1] == ti:
        s2 += ti
      else:
        s2 += s[i]
    s1 = s2
    cnt += 1
  ans = min(cnt,ans)
print(ans)
