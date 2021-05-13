

n, m = map(int, input().split())
a = [[0]+list(map(int, input().split())) for i in range(n)]

# +++ or ---
for i in range(n):
    a[i][0]=a[i][1]+a[i][2]+a[i][3]

a.sort()
ans1=0
ans2=0
for i in range(m):
    ans1-=a[i][0]
    ans2+=a[n-i-1][0]
ansA=max(ans1,ans2)

#++- or --+
for i in range(n):
    a[i][0]=a[i][1]+a[i][2]-a[i][3]
a.sort()
ans3=0
ans4=0
for i in range(m):
    ans3-=a[i][0]
    ans4+=a[n-i-1][0]
ansB=max(ans3,ans4)

#+-+ or -+-
for i in range(n):
    a[i][0]=a[i][1]-a[i][2]+a[i][3]
a.sort()
ans5=0
ans6=0
for i in range(m):
    ans5-=a[i][0]
    ans6+=a[n-i-1][0]
ansC=max(ans5,ans6)

#+-- or -++
for i in range(n):
    a[i][0]=a[i][1]-a[i][2]-a[i][3]
a.sort()
ans7=0
ans8=0
for i in range(m):
    ans7-=a[i][0]
    ans8+=a[n-i-1][0]
ansD=max(ans7,ans8)

print(max(ansA,ansB,ansC,ansD))