a = list(map(int,input().split()))

f = 0
for i in a:
    if i % 2 == 0:
        f = 1

if f:
    ans = 0
else:
    tmp = []
    for i in range(2):
        for j in range(i+1,3):
            tmp.append(a[i] * a[j])
    #print(tmp)
    ans = min(tmp)

print(ans)
