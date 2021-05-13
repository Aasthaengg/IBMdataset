n = int(input())
res = []
for i in range (1,n + 1):
    cnt = 0
    while i % 2 == 0:
        i /= 2
        cnt += 1
    res.append(cnt)
print(res.index(max(res))+1)