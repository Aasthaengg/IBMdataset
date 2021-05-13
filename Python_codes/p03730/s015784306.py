a,b,c=map(int,input().split())
#aの倍数の中でbで割って余りがcになるものが存在すればよい
x=0
for i in range(1,b+1):
    if i*a%b==c:
        x+=1
if x==0:
    print("NO")
else:
    print("YES")