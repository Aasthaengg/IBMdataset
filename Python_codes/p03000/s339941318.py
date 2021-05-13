def cumsum(xs):
    result = [0,xs[0]]
    for x in xs[1:]:
        result.append(result[-1] + x)
    return result
a,b=map(int,input().split())
c=list(map(int,input().split()))
n=cumsum(c)
ans=[]
for i in range(len(n)):
    if n[i]<=b:
        ans.append(n[i])
print(len(ans))