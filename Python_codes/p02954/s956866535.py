s = input()
n = len(s)
s = s.replace('RL','xy')

rls = []
curr_s = 'R'
cnt = 1
ind = 0
for i in range(1,n):
    if s[i] == 'y':
        curr_s = 'y'
        cnt += 1
    elif curr_s == s[i]:
        cnt += 1
    else:
        rls.append((curr_s,cnt,ind))
        ind += cnt
        cnt = 1
        curr_s = s[i]

# if s[-1] != 'y':
rls.append((curr_s,cnt, ind))

# print(s)
# print(rls)

ans = [0]*n
curr_i = 0
for i in range(len(rls)):
    rl_r = 1
    rl_l = 1
    if rls[i][0] == 'y':
        if rls[i-1][0] == 'R':
            rl_r += rls[i-1][1]//2
            rl_l += (rls[i-1][1]+1)//2
        if i+1 < len(rls) and rls[i+1][0] == 'L':
            rl_l += rls[i+1][1]//2
            rl_r += (rls[i+1][1]+1)//2
        ind = rls[i][2]
        ans[ind] = rl_r
        ans[ind+1] = rl_l


print(*ans)