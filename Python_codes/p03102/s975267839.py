n,m,c = list(map(int, input().strip().split()))
b= list(map(int, input().strip().split()))
s = []
for i in range(n):
    array = list(map(int, input().strip().split()))
    s.append(array)
ans=0
for i in range(n):
    x=c
    for j in range(m):
        x+=b[j]*s[i][j]
    if x>0:
        ans=ans+1
print(ans)