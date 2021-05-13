n = int(input())
a = []
ans = []
c = {}
for i in range(n):
    a.append(int(input()))
    ans.append(0)
ans[0] = 1
c[a[0]] = 0
for i in range(1,n):
    if a[i] not in c:
        c[a[i]] = i
    if a[i] == a[i-1]:
        ans[i] = ans[i-1]
    else:
        ans[i] = (ans[i-1] + ans[c[a[i]]]) % 1000000007
        c[a[i]] = i
print(ans[i])