N = int(input())
line = input()
V = [int(n) for n in line.split()]
line = input()
C = [int(n) for n in line.split()]
X=0
Y=0
for i in range(N):
    if V[i] > C[i]:
        X+=V[i]
        Y+=C[i]
print(X-Y)