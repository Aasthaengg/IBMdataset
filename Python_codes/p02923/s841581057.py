n = int(input())
h = list(map(int, input().split()))
ph = h[0]
ans = 0
st = 0
for i in range(1, n):
    if h[i] <= ph:
        st += 1
        ans = max(ans, st)
    else:
        st = 0
    ph = h[i]
print(ans)