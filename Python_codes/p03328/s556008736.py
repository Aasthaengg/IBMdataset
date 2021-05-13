A,B=map(int,input().split())
H=[0]*1000

i=1
while i<=999:
    H[i]=i+H[i-1]
    i+=1

ans=0
while True:
    if (A+ans in H)and(B+ans==H[H.index(A+ans)+1] in H):
        break
    else:
        ans+=1
    
print(ans)