s = list(input())

n = len(s)
ans = [0] * n

for i in range(2):
    cnt = 0
    for j in range(n):
        if s[j] == 'R':
            cnt += 1
        else:
            ans[j] += int(cnt/2)
            ans[j-1] += int((cnt+1)/2)
            cnt = 0
    ans.reverse()
    s.reverse()
    for j in range(n):
        if s[j] == 'L':
            s[j] = 'R'
        else:
            s[j] = 'L'

print(' '.join(map(str, ans)))