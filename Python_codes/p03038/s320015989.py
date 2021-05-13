import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = list(map(int,input().split()))
BC = [tuple(map(int,input().split())) for i in range(m)]
BC = sorted(BC,key=lambda x:-x[1])
cnt = 0
flag = True
while True:
    for b,c in BC:
        A += [c]*b
        cnt += b
        if cnt > n:
            break
    break
A = sorted(A,reverse=True)
print(sum(A[:n]))