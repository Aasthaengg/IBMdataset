N, X, Y = map(int, input().split())

dist_list =[0] *(N+10)
for i in range(1, N):
    for j in range(i+1, N+1):
        dist = min(abs(j-i), abs(X-i)+1+abs(j-Y), abs(Y-i)+1+abs(j-X))
        dist_list[dist] += 1
for k in range(1, N):
    print(dist_list[k])