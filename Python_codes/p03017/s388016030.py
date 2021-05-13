from collections import deque

def dfs(snuke,fnuke):
    global n,a,b,c,d,s
    que = deque()
    que.append([snuke,fnuke])
    lq = 1
    while(lq > 0):
        tmp = que.pop()
        tmps = tmp[0]
        tmpf = tmp[1]
        lq-=1
        if tmps == c and tmpf == d:
            return True
        if tmps+1 != tmpf and s[tmps] =="." and tmps != c:
            que.append([tmps+1,tmpf])
            lq+=1
        elif tmps+2 != tmpf and s[tmps+1] =="." and tmps != c:
            que.append([tmps+2,tmpf])
            lq+=1
        elif tmpf+1 != tmps and s[tmpf] =="." and tmpf != d:
            que.append([tmps,tmpf+1])
            lq+=1
        elif tmpf+2 != tmps and s[tmpf+1] =="." and tmpf != d:
            que.append([tmps,tmpf+2])
            lq+=1
    return False

n,a,b,c,d = map(int,input().split())
s = input()
s += "###"
snuke = a
fnuke = b
if dfs(snuke,fnuke):
    print("Yes")
else:
    print("No")
