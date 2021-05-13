A = []
A += input().split()
A += input().split()
A += input().split()
N = int(input())
b = [input() for _ in range(N)]
 
for i in range(N):
  if b[i] in A:
    A[A.index(b[i])] = '.'
    
if (A[0] == '.' and A[3] == '.' and A[6] == '.') or (A[1] == '.' and A[4] == '.' and A[7] == '.') or (A[2] == '.' and A[5] == '.' and A[8] == '.') or (A[0] == '.' and A[1] == '.' and A[2] == '.') or (A[3] == '.' and A[4] == '.' and A[5] == '.') or (A[6] == '.' and A[7] == '.' and A[8] == '.') or (A[0] == '.' and A[4] == '.' and A[8] == '.') or (A[2] == '.' and A[4] == '.' and A[6] == '.'): print('Yes')
else: print('No')