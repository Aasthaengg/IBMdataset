A = input()
B = input()
tmp = max(len(A),len(B))

A = A.zfill(tmp)
B = B.zfill(tmp)
print('LESS') if A<B else print('GREATER') if A>B else print('EQUAL')