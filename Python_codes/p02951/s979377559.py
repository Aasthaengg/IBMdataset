a,b,c=map(int, input().split())

while c>0:

    if a>=b+1:
        b+=1

    elif a<b+1:
        break
    
    c-=1

print(c)