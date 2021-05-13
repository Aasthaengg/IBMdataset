X = input()
s_cnt = 0
ans = len(X)
for i in range(len(X)):
    if(X[i] == "S"):
        s_cnt += 1
    else:
        if(s_cnt > 0):
            ans -= 2
            s_cnt -= 1
print(ans)