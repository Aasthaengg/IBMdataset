def solve1():
    for i in range(N-1):
        ans.append((i+1,i+2))
        A[i+1]+=A[i]
def solve2():
    for i in reversed(range(1,N)):
        ans.append((i+1,i))
        A[i-1]+=A[i]

N=int(input())
A=list(map(int,input().split()))
l=min(A);r=max(A)
wl=A.index(l);wr=A.index(r)

ans=[]
if l>=0:
    solve1()
elif r<0:
    solve2()
else:
    if abs(l)>abs(r):
        for i in range(N):
            if A[i]>0:
                ans.append((wl+1,i+1))
                A[i]+=l
        solve2()
    else:
        for i in range(N):
            if A[i]<0:
                ans.append((wr+1,i+1))
                A[i]+=r
        solve1()
print(len(ans))
for x,y in ans:
    print(x,y)