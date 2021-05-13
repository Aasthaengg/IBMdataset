k,s = map(int,input().split())

cnt = 0
for i in range(0, k+1):
    #cnt += 1:
        for j in range(0, k+1):
            t = s - i - j
            if t <=k and 0 <= t:
                cnt += 1
            #print(cnt)
            #print(i, j, t)
print(cnt)