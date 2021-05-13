a,b=map(int,input().split())
c=str(a)+str(b)
c=int(c)
for i in range(1001):
    if c==i**2:
        print("Yes")
        exit(0)
print("No")