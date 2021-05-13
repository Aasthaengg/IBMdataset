N = int(input())
lis = list(map(int, input().split()))
lis.sort(reverse=True)
lis = lis[1::2]

ans = 0

for i in range(N):
    ans += lis[i]

print(ans)


