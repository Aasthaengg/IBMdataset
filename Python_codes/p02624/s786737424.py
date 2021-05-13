n=int(input())

bp = [0] * (n+10)
for i in range(2, n+10):
    if bp[i] == 0:
        bp[i] = i
        for j in range(i*i, n+1, i):
            if bp[j]==0:
                bp[j] = i

def fact(n):
    ret=1
    while n>1:
        now=n
        cnt=0
        p=bp[now]
        while now % p == 0:
            now//=p
            cnt+=1
        ret*=cnt+1
        n=now
    return ret

ans=0
for i in range(1,n+1):
    ans += i*fact(i)

print(ans)