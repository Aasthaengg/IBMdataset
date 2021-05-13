a,b,c,d = map(int, input().split())

if abs(a-b) <=d and abs(b-c) <= d:
    print("Yes")
    exit()

elif abs(a-c)<=d:
    print("Yes")
    exit()

else:
    print("No")