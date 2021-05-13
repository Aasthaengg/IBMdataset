N, x = map(int, input().split())
a = sorted(map(int, input().split()))
ans = 0
 
for i in range(N):
    x -= a[i]
    if x < 0:
        break
    else:
        ans += 1
 
print(ans if x <= 0 else ans-1)