N = int(input())
H = list(map(int, input().split()))

ans = 0
ans_ = 0
t = 0 # 
for H in H:
    #print(ans, ans_)
    if t >= H:
        ans_ += 1
    else:
        ans = max(ans, ans_)
        ans_ = 0
    t = H
ans = max(ans, ans_)
print(ans)

