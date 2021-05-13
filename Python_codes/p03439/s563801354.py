N=int(input())
print(N-1)
s=input()
if s=="Vacant":
    exit()
elif s=="Male":
    flag=1
else:
    flag=0
print(0)
s=input()
if s=="Vacant":
    exit()
elif s=="Male":
    flag=1
else:
    flag=0
st=0
end=N-1

while s!="Vacant":
    a=(end+st)//2
    print(a)
    s=input()
    if (a+flag*1)%2:
        if s=="Male":
            st=a
        else:
            end=a
    else:
        if s=="Female":
            st=a
        else:
            end=a
