H,W,D = map(int,input().split())
lis = [0] * (H*W+1)
for i in range(H):
    A = list(map(int,input().split()))
    for j in range(W):
        lis[A[j]] = (i,j)
# print(lis)
com = [0] * (H*W+1)
for i in range(D+1,H*W+1):
    com[i] = com[i-D] + abs(lis[i-D][0]-lis[i][0]) + abs(lis[i-D][1]-lis[i][1])
    #print(i,abs(lis[i-D][0]-lis[i][0]),abs(lis[i-D][1]-lis[i][0]))
    #print(i,lis[i-D][0],lis[i-D][1],lis[i][0],lis[i][1])
# print(lis)
# print(com)
Q = int(input())
for i in range(Q):
    L,R = map(int,input().split())
    print(com[R]-com[L])
