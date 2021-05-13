n,a,b = map(int, input().split())
ans = 0
for i in range(n+1):
    s = 0
    m = str(i)
    for j in range(len(m)):
        s += int(m[j])
    if a <= s <= b:
        ans += i
print(ans)