H=int(input())
W=int(input())
N=int(input())

a=0
count=0
if H>W:
    
    for i in range(W):
        a+=H
        count+=1
        if a>=N:
            break
else:
    for i in range(H):
        a+=W
        count+=1
        if a>=N:
            break
print(count)