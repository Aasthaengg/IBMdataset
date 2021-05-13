n,m,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
la = [0]
lb = [0]
mx = 0
for i in range(n): 
    if la[i] + a[i] > k:
        break
    la.append(la[i]+a[i])
for j in range(m):
    if lb[j] + b[j] > k:
        break
    lb.append(lb[j]+b[j])
now = len(lb)-1
for l in range(len(la)):
    cnt = l
    q = now
    while la[l] + lb[q] > k:
        q -= 1
    now = q
    cnt += q
    if cnt > mx:
        mx = cnt
print(mx)