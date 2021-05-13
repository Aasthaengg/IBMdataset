X,Y,A,B,C=map(int,input().split())
ls_a=list(map(int,input().split()))
ls_b=list(map(int,input().split()))
ls_c=list(map(int,input().split()))

ls_a.sort(reverse=True)
ls_b.sort(reverse=True)
ls_c.sort(reverse=True)

ls=sorted(ls_a[:X]+ls_b[:Y])
ans=sum(ls)
for i in range(min(X+Y, C)):
    if ls[i] < ls_c[i]:
        ans += ls_c[i] - ls[i]
print(ans)