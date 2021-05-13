a=int(input(""))
b=int(input(""))
c=int(input(""))
x=int(input(""))
def countcourse(r,t,y,u):
    cnt=0
    n=0
    for h in range(r+1):
        for l in range(t+1):
            for o in range(y+1):
                if 500*h+100*l+50*o==u:
                    cnt+=1
    return cnt
print(countcourse(a,b,c,x))