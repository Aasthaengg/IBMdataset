x,a=map(int,input().split())
y,b=map(int,input().split())
t=int(input())
if(abs(x-y)<=t*(a-b)):
    print('YES')
else:
    print("NO")
