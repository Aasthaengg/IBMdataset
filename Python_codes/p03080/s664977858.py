N=int(input())
s=str(input())
red=0
blue=0
for i in range(0,N):
    if(s[i]=="R"):
        red+=1
    elif(s[i]=="B"):
        blue+=1
if(red>blue):
    print("Yes")
else:
    print("No")
    
