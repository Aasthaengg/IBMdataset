n,M = map(int,input().split())
d = []
for i in range(n):
    a,b = map(int,input().split())
    d.append([a,b])
 
d.sort(key=lambda x:x[0])

sum_ = 0
cnt = 0
for ab in d:
    if cnt + ab[1] > M:
        sum_ += ab[0] * (M-cnt)
        break
    else:
        cnt += ab[1]
        sum_ += ab[0]*ab[1]
print(sum_)
