n,m = map(int,input().split())
l = []
for _ in range(m):
    a = list(map(int,input().split()))
    l.append(a)

memo = [0]*n

for i in range(m):
    memo[l[i][0]-1] += 1
    memo[l[i][1]-1] += 1

for j in range(n):
    print(memo[j])