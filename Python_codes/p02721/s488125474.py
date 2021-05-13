n,k,c = map(int,input().split())
s = input()

l_used = [False]*(n+1)
r_used = [False]*(n+1)
idx = 0
cnt = 0
while idx < n:
    if s[idx] == 'o':
        l_used[idx] = True
        cnt += 1
        idx += c+1
    else:
        idx += 1
idx = n-1
while idx >= 0:
    if s[idx] == 'o':
        r_used[idx] = True
        idx -= c+1
    else:
        idx -= 1

if cnt == k:
    ans = [] 
    for i in range(n):
        if l_used[i] and r_used[i]:
            ans.append(i+1)
    for i in ans:
        print(i)