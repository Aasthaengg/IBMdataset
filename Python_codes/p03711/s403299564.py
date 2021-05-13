a,b = map(int,input().split())

if a in {1,3,5,7,8,10,12} and b in {1,3,5,7,8,10,12}:
    print("Yes")
elif a in{2} and b in {2}:
    print("Yes")
elif a in {4,6,9,11} and b in {4,6,9,11}:
    print("Yes")   

else:
    print("No")
