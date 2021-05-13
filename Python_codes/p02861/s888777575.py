from itertools import permutations

n = int(input())
v = [list(map(int,input().split())) for i in range(n)]
ans = 0
c = 0
for p in permutations(range(n)):
    c += 1
    arr = [i for i in p]
    for i in range(n-1):
        ans += ((v[arr[i]][0]-v[arr[i+1]][0])**2 + (v[arr[i]][1]-v[arr[i+1]][1])**2)**0.5
ans /= c
print(ans)