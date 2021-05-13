# https://atcoder.jp/contests/arc073/tasks/arc073_a

n,T=map(int,input().split())
t=list(map(int,input().split()))

cnt=T
for i in range(1,n):
    dt=t[i]-t[i-1]
    if dt>=T:
        cnt+=T
    else:
        cnt+=dt
print(cnt)