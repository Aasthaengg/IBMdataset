def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
mod=10**9+7

s=input()+"T"
N=len(s)
x,y=MI()

F=[[],[]]

temp=0
bit=0
for i in range(N):
    if s[i]=="F":
        temp+=1
    else:
        if temp!=0:
            F[bit].append(temp)
        bit=(bit+1)%2
        temp=0
        
XY=[set([0]), set([0])]
    
for bit in range(2):
    for i in range(len(F[bit])):
        temp=set([])
        a=F[bit][i]
        b=-a
        if bit==0 and i==0 and s[0]=="F":
            b=a
        for j in range(len(XY[bit])):
            aaa=XY[bit].pop()
            temp.add(aaa+a)
            temp.add(aaa+b)
        XY[bit]=temp
        
if (x in XY[0] ) and (y in XY[1] ):
    print("Yes")
else:
    print("No")
        


