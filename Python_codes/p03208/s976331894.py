n,k = map(int,input().split())
h = []

for _ in range(n):
    tmp = int(input())
    h.append(tmp)

h.sort()

ans = []
for i in range(n-k+1):
    tmp = h[i+k-1] - h[i]
    ans.append(tmp)
print(min(ans))