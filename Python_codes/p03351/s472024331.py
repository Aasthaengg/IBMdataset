a,b,c,d = [int(x) for x in input().split()]
if abs(b-a)<=d and abs(c-b)<=d:
    print("Yes")
elif abs(c-a)<=d:
    print("Yes")
else:
    print("No")