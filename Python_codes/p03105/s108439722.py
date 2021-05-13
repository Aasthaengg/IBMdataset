S=lambda:input()
I=lambda:int(input())
L=lambda:list(map(int,input().split()))
LS=lambda:list(map(str,input().split()))

a,b,c=L()
ans=0
if a*c<=b:
    ans=c
else:
    ans=b//a
print(ans)