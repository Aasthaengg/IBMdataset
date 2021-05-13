A=int(input())
B=int(input())
C=int(input())
X=int(input())

count=0

for k_a in range(A+1):
    for k_b in range(B+1):
        for k_c in range(C+1):
            if 500*k_a+100*k_b+50*k_c == X:
                count=count+1
print(count)
