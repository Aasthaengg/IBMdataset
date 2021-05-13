n=int(input())
ab=[list(map(int,input().split())) for _ in [0]*(n-1)]
g=[[] for _ in [0]*n]
[g[b-1].append(a-1) for a,b in ab]
[g[a-1].append(b-1) for a,b in ab]

dist_f=[None for _ in [0]*n]
dist_s=[None for _ in [0]*n]
dist_f[0]=0
dist_s[n-1]=0

q=[0]
while q:
    qq=q.pop()
    for i in g[qq]:
        if dist_f[i]==None:
            dist_f[i]=dist_f[qq]+1
            q.append(i)
            
q=[n-1]
while q:
    qq=q.pop()
    for i in g[qq]:
        if dist_s[i]==None:
            dist_s[i]=dist_s[qq]+1
            q.append(i)
            
cnt_f,cnt_s=0,0

for i in range(n):
    if dist_f[i]<=dist_s[i]:
        cnt_f+=1
    else:
        cnt_s+=1
if cnt_f>cnt_s:
    print("Fennec")
else:
    print("Snuke")