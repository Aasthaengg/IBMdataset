n,a,b,c = map(int,input().split())
t = [int(input()) for i in range(n)]
ans = float('inf')
for i in range(1<<(n*2)):
    tmp,cnt,a_t,b_t,c_t = i,0,0,0,0
    for j in range(n):
        if tmp&3==1:
            a_t+=t[j]
            if a_t!=t[j]: cnt+=10
        elif tmp&3==2:
            b_t+=t[j]
            if b_t!=t[j]: cnt+=10
        elif tmp&3==3:
            c_t+=t[j]
            if c_t!=t[j]: cnt+=10
        tmp >>= 2
    if a_t==0 or b_t==0 or c_t==0: continue
    tmp = abs(a-a_t)+abs(b-b_t)+abs(c-c_t)+cnt
    ans = min(ans,tmp)
print(ans)
