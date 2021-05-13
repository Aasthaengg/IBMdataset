x,y,z,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
ans = []
for i in range(x):
    for j in range(y):
        ans.append(a[i]+b[j])
ans.sort(reverse=True)
ans = ans[:k]
ans2 = []
for i in range(len(ans)):
    for j in range(z):
        ans2.append(ans[i]+c[j])
ans2.sort(reverse=True)
for i in range(k):
    print(ans2[i])