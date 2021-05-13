n,l=map(int,input().split())
min =1000
ans = 0
for i in range(n):
    if(min > abs(i+l)):
        min = abs(i+l)
    ans = ans+i+l
if(ans < 0):
    print(ans+min)
else:
    print(ans-min)