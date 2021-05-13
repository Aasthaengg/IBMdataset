H,W,A,B = map(int,input().split())

C = [1]*(W-A) + [0]*A
D = [0]*(W-A) + [1]*A
c = ''
d = ''
for i in C:
    c += str(i)
c = int(c)
for i in D:
    d += str(i)
d = d.zfill(W)

for i in range(H):
    if i < H-B:
        print(c)
    else:
        print(d)