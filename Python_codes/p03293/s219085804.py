s=input()
r=input()
f=0
for i in range(len(r)):
    r=r[-1]+r[:len(r)-1]
    if(r==s):
        print("Yes")
        f=1
        exit()
print("No")