A,B,C,X = [int(input()) for i in range(4)]
X_original = X
n = 0

for i in range(int(A)+1):
    X = X_original
    X500 = X - i*500
    for j in range(int(B)+1):
        X100 = X500 - j*100
        for k in range(int(C)+1):
            X50 = X100-k*50
            if X50== 0:
                n += 1

print(n)