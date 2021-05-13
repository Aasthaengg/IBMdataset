N=int(input())
ba=[list(map(int,input().split()))[::-1]for _ in range(N)]
ba.sort()
 
time=0
ans='Yes'
for b,a in ba:
    time+=a
    if time>b:
        ans='No'
print(ans)