N = int(input())
a = sorted(list(map(int, input().split())))
a2 = a[N:]
ans = 0
for i in range(0, 2*N, 2):
    ans += a2[i]
print(ans)