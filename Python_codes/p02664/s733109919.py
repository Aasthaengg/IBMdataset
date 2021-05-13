t=input()
n=len(t)
a=[0]*n
for i in range(n):
    a[i]=t[i]

for i in range(n):
    if a[i]=="?":
        if i!=n-1:
            if a[i-1]=="D" and a[i+1]=="?":
                a[i]="P"
            elif a[i-1]=="P" and a[i+1]=="?":
                a[i]="D"
            elif a[i-1]=="D" and a[i+1]=="D":
                a[i]="P"
            else:
                a[i]="D"
        else:
            a[i]="D"
    #print(a)

s=''.join(a)
print(s)
