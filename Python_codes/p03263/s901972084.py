h,w = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(h)]
out = []
for i in range(h):
    for j in range(w):
        if A[i][j]&1:
            if j == w-1:
                if i != h-1:
                    A[i+1][j] += 1
                    A[i][j] -= 1
                    out.append((i+1,j+1,i+2,j+1))
            else:
                A[i][j+1] += 1
                A[i][j] -= 1
                out.append((i+1,j+1,i+1,j+2))
print(len(out))
for i,j,k,l in out:
    print(i,j,k,l)