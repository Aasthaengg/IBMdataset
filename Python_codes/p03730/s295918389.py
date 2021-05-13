a,b,c=map(int,input().split())
num=0
for mul in range(10**6):
    num+=a
    num%=b
    if num==c:
        print("YES")
        exit()
print("NO")