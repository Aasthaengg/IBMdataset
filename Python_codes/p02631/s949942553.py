n=int(input(""))
a=[]
ans=[1]
ain=input("").split(" ")
for i in range(n):
    a+=[int(ain[i])]
s=a[1]
for i in range(n-2):
    s^=a[i+2]
ans[0]=s
for i in range(n-1):
    s=s^a[i]
    s^=a[i+1]
    ans+=[s]
b=[]
for i in range(n):
    b+=[str(ans[i])]
print(" ".join(b))


    
