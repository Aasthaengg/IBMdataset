N = int(input())

A = list(map(int,input().split()))
li = []

for i in range(N):
    li.append([A[i],i+1])


li.sort(key=lambda x: x[0])

a = [li[i][1] for i in range(N)]
print(*a)