N = int(input())
a = list(map(int, input().split()))
ans = [0 for j in range(N)]

for i in range(N):
    ans[a[i]-1] = i + 1

print (*ans)
