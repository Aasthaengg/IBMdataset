N=int(input())

A = []
B = []
for i in range(N):
    x1,y1=[int(i) for i in input().split()]
    A.append(x1)
    B.append(y1)

tmp=max(A)
idx=A.index(tmp)
print(tmp+B[idx])

