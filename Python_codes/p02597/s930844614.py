from collections import Counter
N=int(input())
C=list(input())

# RRRRWWWW ok
count=Counter(C)
ws=count["W"]
rs=count["R"]

outws=0
outrs=0
for i in range(N):
    c=C[i]
    if c=="R":
        if not 0<=i<rs:
            outrs+=1
    else:
        if 0<=i<rs:
            outws+=1

ans=max(outrs, outws)
print(ans)