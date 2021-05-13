N = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(N):
    if i < a[i]-1 and a[a[i]-1]-1 == i:
        ans += 1
print(ans)