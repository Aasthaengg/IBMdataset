#=input()
#=int(input())
a,b=map(int,input().split())
#=map(str,input().split())
l=list(map(int,input().split()))
x=0
for i in l:
    x += i
    
y=a-x
if y < 0:
    print(-1)
else:
    print(y)    