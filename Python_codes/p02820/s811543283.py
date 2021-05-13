n, k = map(int,input().split())
r,s,p = map(int, input().split())
t = list(input())
a = [1]*n
for i in range(k,n):
    if t[i] == t[i-k] and a[i-k] == 1:
        a[i] = 0
ans = 0
for j in range(n):
    if t[j] == 'r' and a[j] == 1:
        ans += p
    elif t[j] == 's' and a[j] == 1:
        ans += r
    elif t[j] == 'p' and a[j] == 1:
        ans += s
print(ans)