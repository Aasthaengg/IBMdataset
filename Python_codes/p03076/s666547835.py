#import sys
#input=sys.stdin.read
#*x,=map(int, input().split("\n"))
x=[int(input()) for _ in range(5)]
tmp=100
for i in range(5):
    if x[i]%10:
        tmp = min(tmp,x[i]%10)
        x[i]//=10
        x[i]*= 10
        x[i]+=10
ans= sum(x)
if tmp<100:
    ans-=10
    ans+=tmp
print(ans)
    
