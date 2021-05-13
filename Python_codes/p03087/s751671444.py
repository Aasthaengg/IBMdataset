n,q = map(int,input().split())
s = str(input())
a = [0]
for i in range(1,n):
    if s[i-1] == "A" and s[i] == "C":
        a.append(a[-1]+1)
    else:
        a.append(a[-1])
for j in range(q):
    u,t = map(int,input().split())
    print(a[t-1]-a[u-1])