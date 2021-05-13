n,c,k=map(int,input().split())
t=[]
for _ in range(n):
    t.append(int(input()))
t.sort()

def bus(M):
    j=1
    count=0
    I=t[0]
    for i in range(n):
        if I+k>=t[i] and count<c: 
            count+=1
        else:
            I=t[i]
            count=1
            j+=1
    if j<=M:
        return True
    else:
        return False

start=0
end=n
while end-start>1:
    ty=(start+end)//2
    if bus(ty):
        end=ty
    else:
        start=ty
print(end)