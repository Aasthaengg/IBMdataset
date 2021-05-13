import sys
input = sys.stdin.readline

s = input()[:-1]
ans = 10**18

for a in 'abcdefghijklmnopqrstuvwxyz':
    t = s
    cnt = 0
    
    while t!=a*len(t):
        nt = ''
        
        for i in range(len(t)-1):
            if t[i]==a or t[i+1]==a:
                nt += a
            else:
                nt += t[i]
        
        t = nt
        cnt += 1
    
    ans = min(ans, cnt)

print(ans)