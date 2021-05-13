n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
def zyunretu(s,y):
    l=[]
    for i in range(y,n):
        l.append(s[i])
    l.sort()
    for i in range(len(l)):
        if l[i]==s[y]:
            return i+1
    
def kaizyou(a):
    if a==1:
        return 1
    else:
        return a*kaizyou(a-1)
    
def num(x):
    a=0
    for i in range(n-1):
        a+=(zyunretu(x,i)-1)*kaizyou(n-i-1)
    return a
print(abs(num(p)-num(q)))