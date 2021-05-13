a=input()
b=input()
c=b
res="No"
for i in range(len(a)):
    c=c[-1]+c[:-1]
    if a==c:
        res=("Yes")
        break
print(res)