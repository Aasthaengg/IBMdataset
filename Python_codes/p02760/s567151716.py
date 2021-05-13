# B - Bingo
import itertools
A = list()
for o in range(3):
    a = list(map(int, input().split()))
    A.append(a)
N = int(input())
b = list(int(input()) for p in range(N))#mapオブジェクトにlistをつける

bingo = [A[0],A[1],A[2],[A[0][0],A[1][0],A[2][0]],[A[0][1],A[1][1],A[2][1]],[A[0][0],A[1][1],A[2][2]],[A[0][2],A[1][2],A[2][2]],[A[0][2],A[1][1],A[2][0]]]

B_perm = []    
B = itertools.permutations(b,3)
for i in B:
    B_perm.append(list(i))#タプルをリストに直す

result = 'No'
for j in range(len(B_perm)):
    if B_perm[j] in bingo: 
        result = 'Yes'

print(result)