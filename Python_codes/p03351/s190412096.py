a,b,c,d = map(int,input().split())
count = 0
if abs(b-a) <= d and abs(c-b) <= d:
    count = 1
elif abs(c-a) <= d:
    count = 1
if count != 0:
    print("Yes")
else:
    print("No")