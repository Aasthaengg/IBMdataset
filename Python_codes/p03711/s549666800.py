A = [1,3,5,7,8,10,12]
B = [4,6,9,11]
a,b = map(int, input().split())
if ((a in A)and(b in A)) or ((a in B) and (b in B)) or a == b == 2:
    print("Yes")
else:
    print("No")