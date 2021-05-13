n = int(input())
p = list(map(int, input().split()))

ans = 0
for i, _ in enumerate(p[:-1]):
    #print(p_, i+1)
    p_ = p[i]
    if p_ == i + 1:
        ans += 1
        p[i], p[i+1] = p[i+1], p[i]

if p[-1] == n:
  ans += 1
        
print(ans)

