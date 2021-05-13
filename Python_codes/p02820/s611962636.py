def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

n,k = iim()
r,s,p = iim()
t = list(input())
ans = 0
flag = [True]*n
for i,item in enumerate(t):
    if i >= k and flag[i-k]:
        if t[i] == 'r' and t[i-k] != 'r':
            ans += p
        elif t[i] == 's' and t[i-k] != 's':
            ans += r
        elif t[i] == 'p' and t[i-k] != 'p':
            ans += s
        else:
            flag[i] = False

    else:
        if t[i] == 'r':
            ans += p
        elif t[i] == 's':
            ans += r
        elif t[i] == 'p':
            ans += s

print(ans)