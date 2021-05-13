a,b,c=map(int,input().split())
for i in range(101):
    t=a*i
    if t%b==c:
        print("YES")
        exit()
print("NO")