N = int(input())
X = [list(map(int, input().split())) for _ in range(N)]

X.sort(key=lambda x: x[1])
t = 0
ans = "No"
for a, b in X:
    if t + a > b:
        break
    t += a
else:
    ans = "Yes"
print(ans)

