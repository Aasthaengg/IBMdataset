import sys
H,W = map(int,input().split())
if H < 0 or H > 100 or W < 0 or H > 100:
    sys.exit()
pixeles = []
for I in range(H):
    pixeles.append(str(input()))

print("#"*(W+2))
for L in pixeles:
    print("#",end='')
    print(L,end='')
    print("#")
print("#"*(W+2))
