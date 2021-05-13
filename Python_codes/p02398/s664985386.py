a,b,c = input().split()
a = int(a)
b= int(b)
c=int(c)
aaa = 0
for x in range(a,b+1):
    if c%x == 0:
        aaa+=1
print(aaa)



