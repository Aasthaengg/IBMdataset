def GCD(a,b):
    if(b==0):
        return a 
    return GCD(b,a%b)

def LCM(a,b):
    return a / GCD(a,b) * b


while True:
    try:
        x = list(map(int,input().split()))
        ans_1 = GCD(x[0],x[1])
        ans_2 = LCM(x[0],x[1])
        print("%d %d"%(ans_1,ans_2))
    
    except:
        break
