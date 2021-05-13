N = int(input())
H = list(map(int, input().split()))
ans = H[0]
active = H[0]
for i in range(1,N):
    h = H[i]
    ans += max(0, h - active)
    active = h
print(ans)
