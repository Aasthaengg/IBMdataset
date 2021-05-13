a,b,c,d = map(int, input().split())
if abs(a-c)<=d:
    print("Yes")
elif (abs(a-b)<=d) & (abs(c-b)<=d):
    print("Yes")
else:
    print("No")