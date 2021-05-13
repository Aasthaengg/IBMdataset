s = input()
N = len(s)
x,y = map(int, input().split())
ls = s.split('T')
A = []
B = []
dpx = [0]*(2*N+1)
dpy = [0]*(2*N+1)
for i,c in enumerate(ls):
  if i%2==0:
    A += [len(c)]
  else:
    B += [len(c)]
x -= A[0]
A = A[1:]
dpx[N] = 1
dpy[N] = 1
for a in A:
  dpx = [1 if (i>=a and dpx[i-a]) or (i<=2*N-a and dpx[i+a]) else 0 for i in range(2*N+1)]
for b in B:
  dpy = [1 if (i>=b and dpy[i-b]) or (i<=2*N-b and dpy[i+b]) else 0 for i in range(2*N+1)]
if x>N or y>N:
  print('No')
elif dpx[x+N] and dpy[y+N]:
  print('Yes')
else:
  print('No')