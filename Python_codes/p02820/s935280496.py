N, K = list(map(int,input().split()))
r, s, p = list(map(int,input().split()))
T = input()

ans = 0

def sc(st):
    if st == "p":  return s
    elif st == "r":  return p
    return r

for i in range(K):
    pre = T[i]
    cnt = i
    ans += sc(T[i])
    while(1):
        cnt += K
        if cnt >= N: break 
        if T[cnt] == pre:  pre = "#"
        else:  
            ans += sc(T[cnt])
            pre = T[cnt]
print(ans)