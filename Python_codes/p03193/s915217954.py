N, H, W =(int(i) for i in input().split())
A = [[int(i) for i in input().split()]for i in range(N)]
a = 0

for i in range(N):
    if A[i][0]>=H and A[i][1]>=W:
        a += 1
    else:
        a = a

print(a)
