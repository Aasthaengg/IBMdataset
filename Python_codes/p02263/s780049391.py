s=input().split()
a=[]
for i in s:
    if i in ["+","-","*"]:
        a1=str(a.pop())
        a2=str(a.pop())
        t = eval(a2+i+a1)
        a.append(t)
    else:
        a.append(int(i))
print(a.pop())