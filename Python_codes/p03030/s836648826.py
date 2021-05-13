def resolve():
    n=int(input())
    d=[]
    for i in range(n):
        s,p=input().split()
        d.append([s,100-int(p),i])
    d.sort()
    ans=[0]*n
    for i in range(n):
        ans[i]=d[i][2]
    for m in ans:
        print(m+1)
resolve()