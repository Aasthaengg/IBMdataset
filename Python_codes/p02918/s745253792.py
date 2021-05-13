n,k = map(int, input().split())
s = str(input())

cnt = s.count('RL')
ans = 0

for i in range(0,n-1):
    if s[i] != s[i+1]:
        cnt += 1
    else:
        ans += 1


if cnt >= k:
    ans += 2*k
else:
    ans += 2*cnt
    if k-cnt>=2:
        if s[-1] == 'L' and s[0] == 'L':
            ans += 2
        elif s[-1] == 'L' or s[0] == 'L':
            ans += 1
    else:
        if s[-1] == 'L' or s[0] == 'L':
            ans += 1       


print(min(ans,n-1))