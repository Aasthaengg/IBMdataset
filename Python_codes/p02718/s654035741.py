n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
result='Yes'
for i in range (m):
    if a[len(a)-i-1]/sum(a)<1/(4*m):
        result='No'
        break
print(result)