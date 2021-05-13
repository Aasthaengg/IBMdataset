a,b,c=map(int,input().split())
yn=0
for i in range(1,b+1):
    if (a*i)%b==c:
        yn=1
        break
if yn==1:
    print("YES")
else:
    print("NO")
