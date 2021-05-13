n=int(input())
s=input()
r=''
for i in s:
    r+=i
    if(r*2==s):
        print("Yes")
        break
else:
    print("No")
