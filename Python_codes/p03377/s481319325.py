a,b,x = list(map(int,input().split()))
if x-a<0:
    print("NO")
elif b>=(x-a):
    print("YES")
else:
    print("NO")