h,w = (int(i) for i in input().split())
s = [input() for i in range(h)]
x,v,ans = [[] for i in range(h*w)],[1]*(h*w),0
for i in range(h):
    for j in range(w):
        if i!=h-1 and s[i][j]!=s[i+1][j]:
            x[i*w+j].append((i+1)*w+j)
            x[(i+1)*w+j].append(i*w+j)
        if j!=w-1 and s[i][j]!=s[i][j+1]:
            x[i*w+j].append(i*w+j+1)
            x[i*w+j+1].append(i*w+j)
for i in range(h*w):
    if v[i]:
        q,a,b,v[i] = [i],0,0,0
        while q:
            p = q.pop()
            if s[p//w][p%w]=="#": a+=1
            else: b+=1
            for j in x[p]:
                if v[j]:
                    q.append(j)
                    v[j] = 0
        ans+=a*b
print(ans)