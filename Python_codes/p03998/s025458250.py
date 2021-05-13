s=[]
sa=input()
sb=input()
sc=input()
s.append(sa)
s.append(sb)
s.append(sc)
now=0
while 1:
    if len(s[now])==0:
        break
    if s[now][0]=="a":
        next=0
    elif s[now][0]=="b":
        next=1
    else:
        next=2
    s[now]=s[now][1:]
    now=next
if now==0:
    print("A")
elif now==1:
    print("B")
else:
    print("C")