from collections import deque
h,w = map(int,input().split())
sss = [list(input()) for i in range(h)]


def dfs(a,b):
    d = deque([])
    d.append([a,b])
    n = [1,0,-1,0]
    m = [0,1,0,-1]
    l = [[-1]*w for _ in range(h)]
    l[a][b]=0
    while len(d)!=0:
        #print(l)
        s = d.popleft()
        s1,s2 = s[0],s[1]
        for i in range(4):
            if 0<=s1+m[i] and s1+m[i]<=h-1 and 0<=s2+n[i] and s2+n[i]<=w-1:
                if sss[s1+m[i]][s2+n[i]]=="." and l[s1+m[i]][s2+n[i]]==-1:
                    d.append([s1+m[i],s2+n[i]])
                    l[s1+m[i]][s2+n[i]] = l[s1][s2]+1
    t = 0
    for j in l:
      for m in j:
        t = max(t,m)
    return t
t = 0
for i in range(w):
    for j in range(h):
      if sss[j][i]==".":
        t = max(t,dfs(j,i))
print(t)
