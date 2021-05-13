N, W = map(int, input().split())
wvs = []
for i in range(N):
  w, v = map(int, input().split())
  wvs.append((w, v))
w0 = wvs[0][0]
vs0 = []
vs1 = []
vs2 = []
vs3 = []
for w, v in wvs:
  if w == w0:
    vs0.append(v)
  if w == w0+1:
    vs1.append(v)
  if w == w0+2:
    vs2.append(v)
  if w == w0+3:
    vs3.append(v)
vs0.sort(reverse=True)
vs1.sort(reverse=True)
vs2.sort(reverse=True)
vs3.sort(reverse=True)
#print(w0, vs0, vs1, vs2, vs3)
rs = [0]
for i0 in range(len(vs0)+1):
  for i1 in range(len(vs1)+1):
    for i2 in range(len(vs2)+1):
      for i3 in range(len(vs3)+1):
        if w0*i0+(w0+1)*i1+(w0+2)*i2+(w0+3)*i3 <= W:
          r = sum(vs0[:i0])+sum(vs1[:i1])+sum(vs2[:i2])+sum(vs3[:i3])
          rs.append(r)
r = max(rs)
print(r)
