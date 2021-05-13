A=int(input())
B=int(input())
C=int(input())
X=int(input())
counter=0

for a in range(A+1):
    a_total=a*500
    for b in range(B+1):
        b_total=b*100
        for c in range(C+1):
            c_total=c*50
            total_amount=(a_total+b_total+c_total)
            if X==total_amount:
                counter=counter+1
print(counter)