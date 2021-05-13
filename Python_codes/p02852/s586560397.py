import sys
input=sys.stdin.readline
n,m=map(int,input().split())
t=list(input().rstrip())
s=[]
for i in range(n+1):
    s.append(int(t[n-i]))
ans=[]
now=0
while now<n:
    for i in range(m,0,-1):
        if now+i<=n:
            if s[now+i]==0:
                ans.append(i)
                now=now+i
                break
    else:
        print(-1)
        sys.exit()
ans.reverse()
for i in ans:
    print(i,end='')
    print(' ',end='')





