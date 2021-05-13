a,b,c = (int(x) for x in input().split())
half_pack = int((a+b+c)/2)
if(a == half_pack) and ((b+c) == half_pack):
    print("Yes")
elif(b == half_pack) and ((a+c) == half_pack):
    print("Yes")
elif(c == half_pack) and ((b+a) == half_pack):
    print("Yes")
else:
    print("No")
