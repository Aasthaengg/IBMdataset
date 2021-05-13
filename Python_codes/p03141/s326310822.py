n=int(input())
ab=[]
for i in range(n):
    a,b=map(int,input().split())
    ab.append([a+b,a,b])
ab.sort(reverse=True)
#print(ab)

taka=0
aoki=0

for i in range(1,n+1):
    if i%2!=0:
        taka+=ab[i-1][1]
    else:
        aoki+=ab[i-1][2]
ans=taka-aoki
print(ans)