N = int(input())
a = list(map(int,input().split()))

a = [0] + a
ans = 0
for i in range(N+1):
    if i % 2 == 0:
        continue
    else:
        if a[i] % 2 == 1:
            ans += 1
print(ans)