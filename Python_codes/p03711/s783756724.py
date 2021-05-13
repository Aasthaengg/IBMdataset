lst1=[1,3,5,7,8,10,12]
lst2=[4,6,9,11]
lst3=[2]
a,b=map(int,input().split())
if a in lst1 and b in lst1:
    print("Yes")
elif a in lst2 and b in lst2:
    print("Yes")
elif a in lst3 and b in lst3:
    print("Yes")
else:
    print("No")