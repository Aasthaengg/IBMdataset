# a, b, c, x = map(int, open(0))

A,B,C,X = [int(input()) for i in range(4)]

count = 0

for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if 500*i+100*j+50*k==X:
                count+=1

print(count)