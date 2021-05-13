import sys
input=sys.stdin.buffer.readline
n,c=map(int,input().split())
a=[ [0 for _ in range(10**5+2)] for _ in range(c)]
for _ in range(n):
    s,t,cc=map(int,input().split())
    cc-=1
#    print(s-1,end=' s-1\n')
    #a[cc][s-1]+=1
    #a[cc][t]-=1
    for i in range(s-1,t):
        a[cc][i]=1
'''for i in range(c):
    for j in range(1,10**5+1):
        a[i][j]+=a[i][j-1]
'''
ans=1
for j in range(0,10**5):
    su=0
#    print(c,'hello')
    for i in range(c):
#        print('asdf hello')
#        print(j,i,a[i][j])
        su+=a[i][j]
    ans=max(ans,su)
print(ans)
