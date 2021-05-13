N,K,Q = map(int,input().split())
points = [0]*N

for i in range(Q):
    anchor = (int(input()))-1
    points[anchor] += 1

for i in range(N):
    if K - (Q - points[i]) >0:
        print("Yes")
    else:
        print("No")