stir=input()
lst=stir.split(" ")
l=int(lst[0])
r=int(lst[1])
t=lst[2]
b=1
x=0
multiples=[]
while(b<101):
    multiples.append(int(t)*b)
    b+=1
for a in range(l, r+1):
    for m in multiples:
        if(m==a):
            x+=1
print(x)