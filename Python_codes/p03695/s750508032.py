n=int(input())
a=list(map(int, input().split()))
col=[0]*9
for i in range(n):
    j=min(8, a[i]//400)
    col[j]+=1
zero=0
cnt=0
for c in range(len(col)-1):
    if col[c]==0:
        zero+=1
    else:
        cnt+=1
m=max(cnt,1)
M=cnt+col[-1]
print(m,M)