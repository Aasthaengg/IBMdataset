a,b,c = map(int,input().split())
if pow(c-a-b,2) <= 4*a*b:
    print("No")
elif c-a-b <= 0:
    print("No")
else:
    print("Yes")