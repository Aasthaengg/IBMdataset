h,w,d = map(int,input().split())

whereA = [[0,0] for _ in range(h*w)]
for i in range(h):
    A = list(map(int,input().split()))
    for j,a in enumerate(A):
        whereA[a-1] = [i,j]

Dsum = [0]*(h*w)
for i in range(h*w):
    Dsum[i] = Dsum[max(i-d,i%d)] + abs(whereA[i][0]-whereA[max(i-d,i%d)][0]) + abs(whereA[i][1]-whereA[max(i-d,i%d)][1])

q = int(input())

for _ in range(q):
    l,r = map(int,input().split())
    print(Dsum[r-1] - Dsum[l-1])
