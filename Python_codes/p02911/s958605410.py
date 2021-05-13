n,k,q = map(int,input().split())
point = {}
for i in range(1,n+1):
    point[i] = 0
for j in range(q):
    point[int(input())] += 1
for l in range(1,n+1):
    if k - q + point[l] > 0:
        print("Yes")
    else:
        print("No")