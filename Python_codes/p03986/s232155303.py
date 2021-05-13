X = input()
lis = []
if X[0] == 'S':
    lis.append(0)
cnt = 1
for i in range(1,len(X)):
    if X[i] != X[i-1]:
        lis.append(cnt)
        cnt = 0
    cnt += 1
lis.append(cnt)
if X[-1] == 'T':
    lis.append(0)
else:
    lis += [0,0]
#print(lis)
ans = lis[0]
for i in range(1,len(lis)-2,2):
    if lis[i] < lis[i+1]:
        ans += lis[i+1]-lis[i]
        lis[i+1] -= lis[i]
    else:
        lis[i+2] += lis[i] - lis[i+1]
        lis[i+1] = 0
ans += (lis[-1] + lis[-2])
#print(lis)
print(ans)
