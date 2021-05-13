N = input().strip()
k = len(N)
a = int(N[0])
if k==1:
    cmax = a
else:
    cnt = 0
    for i in range(k):
        cnt += int(N[i])
    cmax = max((a-1)+9*(k-1),cnt)
print(cmax)