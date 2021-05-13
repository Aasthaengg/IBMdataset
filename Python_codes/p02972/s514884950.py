N = int(input())
a = list(map(int, input().split()))
ans = [0 for i in range(N)]
ans2 = []
for i in range(N):
    p = N - 1 - i
    if a[p] != sum(ans[p::p + 1]) % 2:
        ans[p] = 1
        ans2.append(str(p + 1))
print(sum(ans))
print(" ".join(ans2))