A,B,K = (int(T) for T in input().split())
for TK in range(0,K):
    if TK%2==0:
        A -= [0,1][A%2]
        Give = A//2
        A,B  = A-Give,B+Give
    else:
        B -= [0,1][B%2]
        Give = B//2
        A,B  = A+Give,B-Give 
print('{} {}'.format(A,B))