N = int(input())
a = list(map(int, input().split()))
num = set()
ans = 0
for i in range(N):
    # print(a[a[i]-1], a[i])
    if a[a[i]-1] == i+1:
        ans += 1

print(ans//2)
