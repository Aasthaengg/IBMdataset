A=int(input())
B=int(input())
C=int(input())
X=int(input())
p=0
for a in range(0,A+1):  
    for b in range(0,B+1):
        for c in range(0,C+1):
            sum=500*a+100*b+50*c
            if X==sum:
                p=p+1

print(p)