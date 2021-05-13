X = input().strip()
N = len(X)
cnt = 0
tot = 0
for i in range(N):
    if X[i]=="T":
        cnt += 1
    else:
        if cnt>0:
            tot += cnt
            cnt = -1
        else:
            cnt -= 1
print(2*tot)