n=int(input())
L=list(map(int,input().split()))
for i in range(n):
    if L[i]>i+1:
        print(-1)
        exit()
def mal(x):
    if len(x)==0:
        return []
    else:
        t=max(x)
        i=x.index(t)
        k=i-1
        while k>i-t:
            if x[k]>t-i+k:
                t=x[k]
                i=k
            k -= 1
        after=x[:i-t+1]
        before=x[i-t+1:]
        before.remove(t)
        return mal(before)+[t]+mal(after)
ans=mal(L)

for i in range(n):
    print(ans[i])