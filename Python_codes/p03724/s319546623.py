N, M = map(int, input().split())
A = [0]*N
for _ in range(M):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    A[x]+=1
    A[y]+=1
for a in A:
    if a%2:
        print("NO")
        exit()
print("YES")