n, k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

ok = a[-1]
ng = 0
while abs(ok - ng)>1:
    X = (ok + ng)//2
    
    cnt = 0
    for i in range(n):
        temp = a[-(i + 1)]
        if temp <= X:break
        temp_cnt = (temp + X - 1)//X - 1
        cnt += temp_cnt
    
    if cnt <= k:ok = X
    else:ng = X
    
print(ok)