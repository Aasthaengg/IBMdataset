N = input().strip()
k = len(N)
cmax = 0
for i in range(k):
    cmax += int(N[i])
if k>1:
    cnt = (int(N[0])-1)+9*(k-1)
    cmax = max(cmax,cnt)
print(cmax)