n,k=map(int, input().split())
ab=[list(map(int, input().split())) for _ in range(n)]

ab.sort()
total=0
for i in range(n):
    total+=ab[i][1]
    if total>=k:
        print(ab[i][0])
        break
