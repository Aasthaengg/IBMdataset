l = list(map(int, input().split()))
k = int(input())
mx = max(l)
ans = sum(l) - mx
for _ in range(k):
    mx *= 2

print(ans+mx)