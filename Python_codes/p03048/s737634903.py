*RBG, n = map(int, input().split())
RBG.sort()
a, b, c = RBG
ans = 0
for i in range(n//c + 1):
    t = n - c*i
    for j in range(t//b + 1):
        ans += (t - j*b) % a == 0
print(ans)