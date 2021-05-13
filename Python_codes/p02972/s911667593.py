def cin():  return list(map(int,input().split()))

N = cin()[0]
a = cin()

rec = [0 for _ in range(N + 10)]

for i in reversed(range(1, N + 1)):
    cnt = 0
    tmp = i
    while(tmp <= N):
        cnt += rec[tmp]
        tmp += i
    if cnt % 2 == a[i - 1]:  continue
    else:  rec[i] = 1
        
l = []
for i in range(1, N + 1):
    if rec[i]:  l.append(i)
print(len(l))
print(*l)