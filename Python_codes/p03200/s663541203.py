s = list(input())
ans = 0
cnt_w = 0
for i, ss in enumerate(s):
    if ss == 'W':
        ans += i - cnt_w
        cnt_w += 1

print(ans)        
