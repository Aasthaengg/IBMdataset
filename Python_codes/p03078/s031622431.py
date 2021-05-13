x,y,z,k = map(int,input().split())

a = list(map(int,input().split()))

b = list(map(int,input().split()))

c = list(map(int,input().split()))

ab = []
ans = []
for i in range(x):
    for j in range(y):
        ab.append(a[i]+b[j])
ab.sort(reverse=True)

if len(ab) < k:
    for i in range(len(ab)):
        for j in range(z):
            ans.append(ab[i]+c[j])
else:
    for i in range(k):
        for j in range(z):
            ans.append(ab[i]+c[j])

ans.sort(reverse=True)

for i in range(k):
    print(ans[i])