N, T, *t = map(int, open(0).read().split())

end = 0
ans = 0
for i in range(N):
    if t[i] < end:
        ans -= end - t[i]
    end = t[i] + T
    ans += T
print(ans)
