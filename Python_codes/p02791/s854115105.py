n=int(input(""))
pp=input("").split(" ")
latest=n
s=0
for i in range(n):
    tmp=int(pp[i])
    if (tmp<=latest):
        latest=tmp
        s+=1

print(s)
