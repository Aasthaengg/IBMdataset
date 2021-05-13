n,m,l=map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]
B = [list(map(int,input().split())) for _ in range(m)]
for nnum in range(n):
    temp=[]
    for lnum in range(l):
        ret = 0
        for mnum in range(m):
            ret +=(A[nnum][mnum]*B[mnum][lnum])
        temp.append(ret)
    print(*temp)