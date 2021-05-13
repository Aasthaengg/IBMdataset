n = int(input())
a = [int(i) for i in input().split()]
cnt = [0,0]
s = [0,0]

def is_pos(x,i):
    if not x >= 1:
        cnt[i] += 1-x
        s[i] = 1
    return

def is_neg(x,i):
    if not x <= -1:
        cnt[i] += 1+x
        s[i] = -1
    return
    
for i in range(n):
    s[0] += a[i]
    s[1] += a[i]
    x = i%2
    y = (i+1)%2
    is_pos(s[x],x)
    is_neg(s[y],y)

ans = min(cnt)
print(ans)