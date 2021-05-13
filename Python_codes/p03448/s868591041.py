inputlist = [input() for i in range(4)]

n = 0

A,B,C= inputlist[0],inputlist[1],inputlist[2]

for i in range(int(A)+1):

    X = inputlist[3] 

    X = int(X) - i*500

    for j in range(int(B)+1):

        X = X - j*100

        for k in range(int(C)+1):
            
            X = X -k*50

            if X == 0:
                n += 1
            X= X + k*50

        X = X + j*100

    X = X + i*500

print(n)