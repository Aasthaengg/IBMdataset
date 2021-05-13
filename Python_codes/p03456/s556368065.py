a,b=map(int,input().split())

for i in range(int(str(a)+str(b))):
    if (i+1)**2==int(str(a)+str(b)):
        print("Yes")
        break
else:
    print("No")