A=int(input())
B=int(input())
C=int(input())
X=int(input())

sum=[]
count=0
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            s=500*a+100*b+50*c
            if s==X:
                count+=1
                sum.append([a,b,c])

print(count)
