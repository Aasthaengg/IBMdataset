a=input()
s=[]
i=0
total=1000000
while True:
    s=100*int(a[i])+10*int(a[i+1])+int(a[i+2])
    d=abs(s-753)
    if total>d:
        total=d
    i+=1
    if i+2==len(a):
        print(total)
        break