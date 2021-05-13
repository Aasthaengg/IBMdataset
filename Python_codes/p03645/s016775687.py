n,m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
w = [0]*(n+1)
for i,j in a:
    if (i==1):
        w[j] = 1
for i,j in a:
    if (j==n):
        if (w[i]==1):
            print("POSSIBLE")
            exit()
print("IMPOSSIBLE")    