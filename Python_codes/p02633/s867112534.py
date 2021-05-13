x=int(input())
t=0
i=1
while True:
    t+=x
    t%=360
    if t==0:
        print(i)
        break
    i+=1