N, A, B = map(int, input().split())
vs = list(map(int, input().split()))
vs.sort(reverse=True)
#print(vs)
r = sum(vs[:A])/A
print(r)
vA = vs[A-1]
I = vs.index(vA)
C = vs.count(vA)
#print(I, C)
if I != 0:
  # C_{C}_{A-I}
  r = 1
  for i in range(1, A-I+1):
    r = r*(C-i+1)//i
  print(r)
else:
  rs = []
  for n in range(A, B+1):
    # C_{C}_{N-I}
    if n-I < 0 or n-I > C:
      continue
    r = 1
    for i in range(1, n-I+1):
      r = r*(C-i+1)//i
    #print(C, n-I, r)
    rs.append(r)
  #print(rs)
  r = sum(rs)
  print(r)
