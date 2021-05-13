A, B, C, D = map(int, input().split())
 
# X=ceil(A/D)とY=ceil(C/B)を比較し、X>=Yなら勝ち、X<Yなら負け
X = (A+D-1) // D
Y = (C+B-1) // B
if X >= Y: print('Yes')
else: print('No')