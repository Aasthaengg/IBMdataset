N = int(input())
a = list(map(int, input().split()))
ans = 0

l = sorted(a, reverse=True)

for i in range(N):
    ans += l[2*i+1]

print(ans)