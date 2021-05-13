a=int(input())
b=int(input())
d=[a,b]
c=[1,2,3]
for i in range(0,len(c)):
    if(c[i] not in d):
        print(c[i])
        break