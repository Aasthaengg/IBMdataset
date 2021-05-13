a=input()
ok=True
for i in range(len(a)):
    if (i+1)%2==0 and a[i]=="R":
        ok=False
        break
    if (i+1)%2==1 and a[i]=="L":
        ok=False
        break
 
if ok:
    print("Yes")
else:
    print("No")