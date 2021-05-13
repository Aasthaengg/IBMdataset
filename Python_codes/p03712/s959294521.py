h,w=map(int,input().split())
A=[list(input()) for i in range(h)]
B=[['#' for i in range(w+2)] for i in range(h+2)]
for i in range(h):
    for j in range(w):
        B[i+1][j+1]=A[i][j]
for b in B:
    print(''.join(b))