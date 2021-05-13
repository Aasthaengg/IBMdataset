s=input()
p=True
t=""
l=s
while p==True:
    p=False
    f=l[0:8]
    if f=="dreamera":
        t +="dream"
        l=l[5:]
        p=True
    f=l[0:7]
    if p==False and f=="dreamer":
        t += "dreamer"
        l=l[7:]
        p=True
    f=l[0:6]
    if p==False and f=="eraser":
        t+="eraser"
        l=l[6:]
        p=True
    f=l[0:5]
    if p==False and f=="erase":
        t+="erase"
        l=l[5:]
        p=True
    if p==False and f=="dream":
        t+="dream"
        l=l[5:]
        p=True
if s==t:
    print("YES")
else:
    print("NO")