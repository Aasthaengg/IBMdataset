N=int(input())
A=list(map(int,input().split()))
x=0
for a in A:
    x^=a
ans=''
for a in A:
    ans+=str(x^a)+' '
print(ans)
