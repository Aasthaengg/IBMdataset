s=input().split();
x=int(s[0])
y=int(s[1])
list1=[2]
list2=[4,6,9,11]
list3=[1,3,5,7,8,10,12]
ans=0;
if((x in list1) and (y in list1)): ans=1
elif((x in list2) and (y in list2)):ans=1
elif((x in list3) and (y in list3)):ans=1
if(ans==1):print("Yes")
else:print("No")
    

