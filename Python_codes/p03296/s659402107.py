n = int(input())
x = list(map(int,input().split()))
x.append('?')
ch = 1
ans = 0
for i in range(1,n+1):
    if x[i]==x[i-1]:
        ch+=1
    else:
        ans+=ch//2
        ch=1
print(ans)
