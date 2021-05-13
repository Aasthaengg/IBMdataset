x,y,z,k=map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
c=list(map(int, input().split()))

ab=[]
for i in range(x):
    for j in range(y):
        ab.append(a[i]+b[j])

if len(ab)>k:
    ab.sort(reverse=True)
    ab=ab[:k]
else:
    ab.sort(reverse=True)

ans=[]
for i in range(len(ab)):
    for j in range(z):
        ans.append(ab[i]+c[j])
ans.sort(reverse=True)

for i in range(k):
    print(ans[i])

