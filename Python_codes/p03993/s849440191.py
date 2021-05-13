n = int(input())
a = list(map(int, input().split()))

like = {}
ans = 0

for i, r in enumerate(a):
    like[i+1] = r
    if r in like and like[r] == i+1:
        ans += 1

print(ans)
