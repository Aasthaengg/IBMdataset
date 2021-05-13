N = int(input())

if N == 0:
    print(2)
    exit()
elif N == 1:
    print(1)
    exit()

L_2 = 2
L_1 = 1
for i in range(N-1):
    L = L_1+L_2
    L_2 = L_1
    L_1 = L
print(L)
