printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

h,w = inm()
a = []
seq = []
for i in range(h):
    a.append(inl())
for i in range(h):
    for j in range(w-1):
        if a[i][j]%2==1:
            seq.append((i,j,i,j+1))
            a[i][j+1] += 1
    if a[i][w-1]%2==1 and i<h-1:
        seq.append((i,w-1,i+1,w-1))
        a[i+1][w-1] += 1
print(len(seq))
for z in seq:
    print("{} {} {} {}".format(z[0]+1,z[1]+1,z[2]+1,z[3]+1))
