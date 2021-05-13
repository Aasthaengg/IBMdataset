n,k = map(int,input().split())
s = input()
flag = [0]*n
f = s[0]
cnt  = 0
for i,t in enumerate(s):
    if t == 'L':
        if i != 0 and s[i-1] == 'L':
            flag[i] = 1
    if t == 'R':
        if i != n-1 and s[i+1] == 'R':
            flag[i] = 1
    if t == f and i != n-1 and s[i+1] != f:
        cnt += 1
ans = sum(flag)
if s[-1] == f:
    ans += min(k,cnt)*2
else:
    ans += 2*cnt - 1 if cnt <= k else 2*k
print(ans)
