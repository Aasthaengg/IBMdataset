k=int(input())
a=[]
for i in range(1,10):
    a.append(i)
s=0
t=8
for i in range(1,10):
    for j in range(s,t+1):
        if str(a[j])[len(str(a[j]))-1]=="0":
            a.append(str(a[j])+"0")
            a.append(str(a[j])+"1")
        elif str(a[j])[len(str(a[j]))-1]=="9":
            a.append(str(a[j])+"8")
            a.append(str(a[j])+"9")
        else:
            c=int(str(a[j])[len(str(a[j]))-1])-1
            d=int(str(a[j])[len(str(a[j]))-1])
            e=int(str(a[j])[len(str(a[j]))-1])+1
            a.append(str(a[j])+str(c))
            a.append(str(a[j])+str(d))
            a.append(str(a[j])+str(e))
    s=t+1
    t=len(a)-1
print(a[k-1])