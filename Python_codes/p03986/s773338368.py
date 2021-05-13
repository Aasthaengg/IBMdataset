X = input().rstrip()
cnt = 0
res = len(X)
for x in X:
    if x=="S":
        cnt += 1
    else:
        if cnt > 0:
            res -= 2
            cnt -= 1
print(res)