n,m = map(int,input().split())
s = [0] * m
k = [0] * m
for i in range(m):
    s[i] = list(map(int,input().split()))
    k[i] = s[0]
    s[i] = s[i][1:]
p = list(map(int,input().split()))

ans = 0
b = '0' + str(n) + 'b'
for i in range(1 << n):
    sw = format(i,b)
    if all(sum(sw[g-1] == '1' for g in s[j])%2 == p[j] for j in range(m)):
        ans += 1
print(ans)
