n,m = map(int,input().split())
point = [0] * n
cnt = 0
for i in range(m):
    a,b = map(int,input().split())
    point[a-1] += 1
    point[b-1] += 1
    # if a > b:
    #     a,b = b,a
    # for j in range(a,b):
    #     edge[j-1] += 1
for i in range(len(point)):
    if point[i] % 2 == 1:
        print("NO")
        exit()
print("YES")


