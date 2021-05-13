def cP(x):
    if x%2==0 or x%3==0 or x%5==0 :
        return 0
    for i in range(7,int(x**0.5+1),2):
        if x%i==0:
            return 0
    return 1


x = int(input())
if x==2 or x==3 or x==5 :
    print(x)
    exit()

if x%2==0 :
    x+=1

while 1:
    if cP(x) :
        break
    #print(x)
    x+=2

print(x)

