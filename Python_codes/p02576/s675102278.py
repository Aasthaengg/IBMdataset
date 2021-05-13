y = input('')
Y = y.split()
N = int(Y[0])
X = int(Y[1])
T = int(Y[2])
if N%X == 0:
    t = T * N//X
elif N%X != 0:
    t = T * (N//X + 1)
print(t)