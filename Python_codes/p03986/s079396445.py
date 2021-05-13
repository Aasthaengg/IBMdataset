S = str(input())
ans = 0
s_ctr = 0
# s の後の t をひたすら省く
for i in range(len(S)):
    if S[i] == "S":
        s_ctr += 1
    else:
        if s_ctr > 0:
            ans += 1
            s_ctr -= 1
print(len(S) - ans * 2)