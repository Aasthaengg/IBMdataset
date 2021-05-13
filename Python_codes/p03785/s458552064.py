n,c,k = map(int,input().split())
t_input = [int(input()) for i in range(n)]

t_s = sorted(t_input)

ans = 1
c_limit = 1
t_limit = t_s[0]+k
for i in range(1,n):
    t = t_s[i]
    #乗客が前の客の時間制限より大きいか、すでにバスが定員以上なら
    if t>t_limit or c_limit>=c:
        ans+=1
        c_limit=1
        t_limit = t+k
    else:
        c_limit+=1
print(ans)