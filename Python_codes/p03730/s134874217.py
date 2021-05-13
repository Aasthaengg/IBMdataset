a,b,c=map(int,input().split())
res="NO"
x=a-b
for i in range(100):
    if (x*i)%b==c:
        res="YES"
print(res)