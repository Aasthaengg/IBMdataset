N, T = list(map(int, input().split()))
A = list(map(int, input().split()))

im = 0
m = 10**20
B = []
C = []
for i,a in enumerate(A):
    if a<m:
        m=a
        im=i
    B.append(a-m)
    C.append(im)

maxB = max(B)
print(len({c for b,c in zip(B,C) if b==maxB}))