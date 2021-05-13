X = input()
s_cnt = 0
ans = 0
for s in X:
    if s=='S':
        s_cnt += 1
    else:
        if s_cnt > 0:
            ans += 1
            s_cnt -= 1

print(len(X) - 2*ans)
