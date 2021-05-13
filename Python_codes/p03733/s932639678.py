n,t = map(int,input().split())
t_li = list(map(int,input().split()))

cnt = 0
ans = 0
for i in range(n):
    if i == 0:
        before = t_li[i]
        ans = t_li[i] + t
        continue
    
    if ans < t_li[i]:
        cnt += t_li[i] - ans
        ans = t_li[i] + t
    else:
        ans = t_li[i] + t
        
print(ans - cnt)