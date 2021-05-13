N, K = (int(i) for i in input().split())
l = [int(i) for i in input().split()]

l.sort()
ans = 0
for i in range(1, K+1):
    ans += l[-i]
print(ans)
