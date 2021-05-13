N=int(input())
D=list(map(int,input().split()))
M=int(input())
T=list(map(int,input().split()))
d,t={},{}
for key in D:
    if key in d:
        d[key]+=1
    else:
        d[key]=1
for key in T:
    if key in t:
        t[key]+=1
    else:
        t[key]=1
flag=True
for key in list(set(T)):
    if key not in d or t[key]>d[key]:
        flag=False
print("YES" if flag else "NO")