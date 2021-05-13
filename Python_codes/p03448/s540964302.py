A=int(input())
B=int(input())
C=int(input())
X=int(input())
ans=0

for a in range(A+1):
    if X < 500*a:
        break
    for b in range(B+1):
        if X < 500*a+100*b:
            break
        for c in range(C+1):
            if X == 500*a+100*b+50*c:
                ans+=1
print(ans)